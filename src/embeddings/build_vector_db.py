"""
Vector Database Builder - Create FAISS index from documents
"""

import os
import sys
import pickle
import logging
from pathlib import Path
from typing import List, Dict
import numpy as np

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

try:
    import faiss
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("ERROR: Required packages not installed.")
    print("Run: pip install faiss-cpu sentence-transformers")
    sys.exit(1)

from embeddings.document_processor import DocumentProcessor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VectorDBBuilder:
    """Build FAISS vector database from documents"""

    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """
        Args:
            model_name: SentenceTransformer model name
        """
        logger.info(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)
        self.embedding_dim = self.model.get_sentence_embedding_dimension()

    def create_embeddings(self, chunks: List[Dict[str, str]]) -> np.ndarray:
        """
        Create embeddings for all chunks

        Args:
            chunks: List of chunk dicts with 'text' key

        Returns:
            NumPy array of embeddings (shape: [num_chunks, embedding_dim])
        """
        texts = [chunk['text'] for chunk in chunks]

        logger.info(f"Creating embeddings for {len(texts)} chunks...")
        embeddings = self.model.encode(
            texts,
            show_progress_bar=True,
            batch_size=32,
            convert_to_numpy=True
        )

        logger.info(f"Embeddings shape: {embeddings.shape}")
        return embeddings

    def build_faiss_index(self, embeddings: np.ndarray) -> faiss.Index:
        """
        Build FAISS index from embeddings

        Args:
            embeddings: NumPy array of embeddings

        Returns:
            FAISS index
        """
        logger.info("Building FAISS index...")

        # Use IndexFlatIP for cosine similarity (with normalized vectors)
        index = faiss.IndexFlatIP(self.embedding_dim)

        # Normalize embeddings for cosine similarity
        faiss.normalize_L2(embeddings)

        # Add to index
        index.add(embeddings)

        logger.info(f"FAISS index built with {index.ntotal} vectors")
        return index

    def save_index(self, index: faiss.Index, chunks: List[Dict], output_dir: str):
        """
        Save FAISS index and chunk metadata

        Args:
            index: FAISS index
            chunks: List of chunk dicts
            output_dir: Directory to save files
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Save FAISS index
        index_file = output_path / "faiss_index.bin"
        faiss.write_index(index, str(index_file))
        logger.info(f"Saved FAISS index: {index_file}")

        # Save chunk metadata
        chunks_file = output_path / "chunks_metadata.pkl"
        with open(chunks_file, 'wb') as f:
            pickle.dump(chunks, f)
        logger.info(f"Saved chunk metadata: {chunks_file}")

        # Save build info
        info_file = output_path / "build_info.txt"
        with open(info_file, 'w') as f:
            f.write(f"Total chunks: {len(chunks)}\n")
            f.write(f"Embedding dimension: {self.embedding_dim}\n")
            f.write(f"Model: {self.model}\n")
            f.write(f"Index type: {type(index).__name__}\n")
        logger.info(f"Saved build info: {info_file}")


def main():
    """Main build pipeline"""
    # Paths
    project_root = Path(__file__).parent.parent.parent
    data_dir = project_root / "data"
    docs_dir = data_dir / "documents"
    output_dir = data_dir / "vector_db"

    logger.info("=" * 60)
    logger.info("IPTVBoss Support Agent - Vector DB Builder")
    logger.info("=" * 60)

    # Check if documents directory exists
    if not docs_dir.exists():
        logger.error(f"Documents directory not found: {docs_dir}")
        logger.info("Please copy documents to data/documents/ first")
        return

    # Step 1: Process documents
    logger.info("\n[1/4] Processing documents...")
    processor = DocumentProcessor(chunk_size=5000, chunk_overlap=1000)
    documents = processor.load_documents(str(docs_dir))

    if not documents:
        logger.error("No documents found!")
        return

    # Step 2: Chunk documents
    logger.info("\n[2/4] Chunking documents...")
    chunks = processor.chunk_documents(documents)
    chunks = processor.extract_metadata(chunks)

    # Step 3: Create embeddings
    logger.info("\n[3/4] Creating embeddings...")
    builder = VectorDBBuilder()
    embeddings = builder.create_embeddings(chunks)

    # Step 4: Build and save index
    logger.info("\n[4/4] Building FAISS index...")
    index = builder.build_faiss_index(embeddings)
    builder.save_index(index, chunks, str(output_dir))

    logger.info("\n" + "=" * 60)
    logger.info("✅ Vector database built successfully!")
    logger.info(f"📁 Output location: {output_dir}")
    logger.info(f"📊 Total chunks: {len(chunks)}")
    logger.info(f"📊 Total documents: {len(documents)}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
