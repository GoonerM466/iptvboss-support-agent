"""
Vector Search - FAISS-based semantic search for document retrieval
"""

import pickle
import logging
from pathlib import Path
from typing import List, Dict, Tuple
import numpy as np

try:
    import faiss
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("ERROR: Required packages not installed.")
    print("Run: pip install faiss-cpu sentence-transformers")
    raise

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VectorSearch:
    """Semantic search using FAISS vector database"""

    def __init__(self, vector_db_path: str, model_name: str = 'all-MiniLM-L6-v2'):
        """
        Args:
            vector_db_path: Path to directory containing FAISS index and metadata
            model_name: SentenceTransformer model name (must match build model)
        """
        self.vector_db_path = Path(vector_db_path)
        self.model = SentenceTransformer(model_name)

        # Load FAISS index
        index_file = self.vector_db_path / "faiss_index.bin"
        if not index_file.exists():
            raise FileNotFoundError(f"FAISS index not found: {index_file}")

        self.index = faiss.read_index(str(index_file))
        logger.info(f"Loaded FAISS index with {self.index.ntotal} vectors")

        # Load chunk metadata
        chunks_file = self.vector_db_path / "chunks_metadata.pkl"
        if not chunks_file.exists():
            raise FileNotFoundError(f"Chunk metadata not found: {chunks_file}")

        try:
            with open(chunks_file, 'rb') as f:
                self.chunks = pickle.load(f)
        except UnicodeDecodeError:
            # Try with different encoding
            with open(chunks_file, 'rb') as f:
                self.chunks = pickle.load(f, encoding='latin1')
        logger.info(f"Loaded {len(self.chunks)} chunk metadata entries")

    def search(
        self,
        query: str,
        top_k: int = 5,
        min_score: float = 0.3
    ) -> List[Dict[str, any]]:
        """
        Search for most relevant chunks

        Args:
            query: User query string
            top_k: Number of results to return
            min_score: Minimum similarity score (0-1, higher is more similar)

        Returns:
            List of dicts with 'text', 'source', 'score', and other metadata
        """
        # Encode query
        query_embedding = self.model.encode([query], convert_to_numpy=True)

        # Normalize for cosine similarity
        faiss.normalize_L2(query_embedding)

        # Search FAISS index
        scores, indices = self.index.search(query_embedding, top_k)

        # Build results
        results = []
        for score, idx in zip(scores[0], indices[0]):
            # Filter by minimum score
            if score < min_score:
                continue

            # Get chunk metadata
            chunk = self.chunks[idx].copy()
            chunk['score'] = float(score)
            results.append(chunk)

        logger.debug(f"Query: '{query}' -> {len(results)} results (min_score={min_score})")
        return results

    def search_with_context(
        self,
        query: str,
        top_k: int = 3,
        min_score: float = 0.3
    ) -> Tuple[str, List[Dict]]:
        """
        Search and format results as context string for LLM

        Args:
            query: User query
            top_k: Number of results
            min_score: Minimum similarity score

        Returns:
            Tuple of (context_string, results_list)
        """
        results = self.search(query, top_k=top_k, min_score=min_score)

        if not results:
            return "", results

        # Format context
        context_parts = []
        for i, result in enumerate(results, 1):
            context_parts.append(f"--- Document {i} (from {result['source']}) ---")
            context_parts.append(result['text'])
            context_parts.append("")  # Blank line

        context = "\n".join(context_parts)
        return context, results

    def get_similar_chunks(self, chunk_id: str, top_k: int = 3) -> List[Dict]:
        """
        Find chunks similar to a given chunk (for related content)

        Args:
            chunk_id: ID of source chunk
            top_k: Number of similar chunks to return

        Returns:
            List of similar chunk dicts
        """
        # Find chunk by ID
        chunk_idx = None
        for idx, chunk in enumerate(self.chunks):
            if chunk['chunk_id'] == chunk_id:
                chunk_idx = idx
                break

        if chunk_idx is None:
            logger.warning(f"Chunk ID not found: {chunk_id}")
            return []

        # Get embedding for this chunk
        chunk_embedding = self.index.reconstruct(chunk_idx)
        chunk_embedding = np.expand_dims(chunk_embedding, axis=0)

        # Search for similar
        scores, indices = self.index.search(chunk_embedding, top_k + 1)

        # Build results (skip first result which is the chunk itself)
        results = []
        for score, idx in zip(scores[0][1:], indices[0][1:]):
            chunk = self.chunks[idx].copy()
            chunk['score'] = float(score)
            results.append(chunk)

        return results


def main():
    """Test vector search"""
    import sys
    from pathlib import Path

    # Add parent to path
    sys.path.append(str(Path(__file__).parent.parent))

    # Initialize search
    project_root = Path(__file__).parent.parent.parent
    vector_db_path = project_root / "data" / "vector_db"

    if not vector_db_path.exists():
        print(f"ERROR: Vector DB not found at {vector_db_path}")
        print("Run: python src/embeddings/build_vector_db.py first")
        return

    searcher = VectorSearch(str(vector_db_path))

    # Test queries
    test_queries = [
        "How do I set up Dropbox?",
        "My EPG isn't showing",
        "Database won't load",
        "What's the difference between M3U and XC?"
    ]

    print("\n" + "=" * 60)
    print("Vector Search Test")
    print("=" * 60)

    for query in test_queries:
        print(f"\nQuery: {query}")
        print("-" * 60)

        results = searcher.search(query, top_k=3, min_score=0.3)

        for i, result in enumerate(results, 1):
            print(f"\n[{i}] Score: {result['score']:.3f} | Source: {result['source']}")
            print(f"Preview: {result['text'][:150]}...")


if __name__ == "__main__":
    main()
