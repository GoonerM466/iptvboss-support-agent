"""
Document Processor - Loads and chunks markdown documents for embedding
"""

import os
import re
import yaml
from pathlib import Path
from typing import List, Dict, Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DocumentProcessor:
    """Process markdown documents into chunks for embedding"""

    def __init__(self, config_path: str = None):
        """
        Args:
            config_path: Path to settings.yaml (optional, defaults to config/settings.yaml)
        """
        # Load settings from YAML
        if config_path is None:
            config_path = Path(__file__).parent.parent.parent / "config" / "settings.yaml"

        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        # Extract document processing settings
        doc_config = config['document_processing']
        self.split_files = doc_config.get('split_files', False)
        self.chunk_size = doc_config.get('chunk_size', 5000)
        self.chunk_overlap = doc_config.get('chunk_overlap', 1000)
        self.max_file_size = doc_config.get('max_file_size', 15000)

        logger.info(f"Document Processor initialized:")
        logger.info(f"  split_files: {self.split_files}")
        logger.info(f"  chunk_size: {self.chunk_size}")
        logger.info(f"  chunk_overlap: {self.chunk_overlap}")
        logger.info(f"  max_file_size: {self.max_file_size}")

    def load_documents(self, docs_dir: str) -> List[Dict[str, str]]:
        """
        Load all markdown files from a directory

        Args:
            docs_dir: Path to directory containing markdown files

        Returns:
            List of dicts with 'content', 'source', and 'title' keys
        """
        docs = []
        docs_path = Path(docs_dir)

        if not docs_path.exists():
            raise FileNotFoundError(f"Directory not found: {docs_dir}")

        # Load all .md files
        for md_file in docs_path.rglob("*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                # Extract title from first heading or filename
                title = self._extract_title(content) or md_file.stem

                docs.append({
                    'content': content,
                    'source': str(md_file.relative_to(docs_path.parent)),
                    'title': title
                })
                logger.info(f"Loaded: {md_file.name} ({len(content)} chars)")

            except Exception as e:
                logger.error(f"Error loading {md_file}: {e}")

        logger.info(f"Total documents loaded: {len(docs)}")
        return docs

    def _extract_title(self, content: str) -> str:
        """Extract title from first # heading"""
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        return match.group(1) if match else ""

    def chunk_documents(self, documents: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Split documents into overlapping chunks

        Args:
            documents: List of document dicts from load_documents()

        Returns:
            List of chunk dicts with 'text', 'source', 'title', and 'chunk_id' keys
        """
        chunks = []

        for doc in documents:
            content = doc['content']
            source = doc['source']
            title = doc['title']

            # Split by sections (## headings) first for better semantic chunks
            sections = self._split_by_sections(content)

            for section_idx, section in enumerate(sections):
                section_chunks = self._chunk_text(section)

                for chunk_idx, chunk_text in enumerate(section_chunks):
                    chunks.append({
                        'text': chunk_text,
                        'source': source,
                        'title': title,
                        'chunk_id': f"{source}_{section_idx}_{chunk_idx}"
                    })

        logger.info(f"Created {len(chunks)} chunks from {len(documents)} documents")
        return chunks

    def _split_by_sections(self, content: str) -> List[str]:
        """
        Split document into sections based on configuration

        If split_files=False: Keep file intact (unless exceeds max_file_size)
        If split_files=True: Split on ## headings as before
        """
        file_size = len(content)

        # Priority 1: If split_files is disabled, keep file intact
        if not self.split_files:
            # Safety check: if file is HUGE, split it anyway
            if file_size > self.max_file_size:
                logger.warning(f"File exceeds max_file_size ({file_size} > {self.max_file_size}). Forcing split.")
                # Fall through to splitting logic below
            else:
                logger.debug(f"Keeping file intact ({file_size} chars)")
                return [content]

        # Priority 2: If split_files=True or file too large, split normally
        # Split on #### (level 4 headings) but keep the heading
        sections = re.split(r'(^####\s+.+$)', content, flags=re.MULTILINE)

        # Combine headings with their content
        combined = []
        for i in range(1, len(sections), 2):
            if i + 1 < len(sections):
                section_content = sections[i] + sections[i + 1]
                # Keep sections together unless extremely large (> 5000 chars)
                combined.append(section_content)
            else:
                combined.append(sections[i])

        # If no #### sections found, try ## sections
        if not combined:
            sections = re.split(r'(^##\s+.+$)', content, flags=re.MULTILINE)
            for i in range(1, len(sections), 2):
                if i + 1 < len(sections):
                    combined.append(sections[i] + sections[i + 1])
                else:
                    combined.append(sections[i])

        # If still no sections found, return whole content
        return combined if combined else [content]

    def _chunk_text(self, text: str) -> List[str]:
        """
        Split text into overlapping chunks

        Args:
            text: Text to chunk

        Returns:
            List of text chunks
        """
        if len(text) <= self.chunk_size:
            return [text]

        chunks = []
        start = 0
        text_len = len(text)

        while start < text_len:
            end = min(start + self.chunk_size, text_len)

            # Try to break at paragraph boundary
            if end < text_len:
                # Look for paragraph break
                paragraph_break = text.rfind('\n\n', start, end)
                if paragraph_break > start:
                    end = paragraph_break
                else:
                    # Try to break at sentence
                    sentence_break = text.rfind('. ', start, end)
                    if sentence_break > start:
                        end = sentence_break + 1

            # Extract chunk
            chunk = text[start:end].strip()
            if chunk:  # Only add non-empty chunks
                chunks.append(chunk)

            # Move to next chunk with overlap
            next_start = end - self.chunk_overlap

            # Prevent infinite loop - ensure we always move forward
            if next_start <= start:
                start = end
            else:
                start = next_start

            # Safety check - if we're not making progress, break
            if start >= text_len:
                break

        return chunks

    def extract_metadata(self, chunks: List[Dict[str, str]]) -> List[Dict]:
        """
        Extract metadata from chunks for better retrieval

        Args:
            chunks: List of chunk dicts

        Returns:
            Chunks with additional metadata
        """
        for chunk in chunks:
            text = chunk['text']

            # Detect keywords for image mapping
            chunk['keywords'] = self._extract_keywords(text)

            # Detect if chunk contains steps/procedures
            chunk['has_steps'] = bool(re.search(r'^\d+\.|^-\s|^\*\s', text, re.MULTILINE))

            # Detect if chunk is troubleshooting-related
            chunk['is_troubleshooting'] = any(
                keyword in text.lower()
                for keyword in ['error', 'issue', 'problem', 'fix', 'solution', 'troubleshoot']
            )

        return chunks

    def _extract_keywords(self, text: str) -> List[str]:
        """Extract important keywords from text"""
        # Common IPTVBoss-specific terms
        keywords = []
        keyword_patterns = [
            r'\bdropbox\b', r'\bgoogle drive\b', r'\bepg\b', r'\bxc server\b',
            r'\blayout\b', r'\bsource\b', r'\bplaylist\b', r'\bm3u\b',
            r'\biptv\b', r'\bchannels?\b', r'\bproviders?\b', r'\bdatabase\b'
        ]

        text_lower = text.lower()
        for pattern in keyword_patterns:
            if re.search(pattern, text_lower):
                keywords.append(re.search(pattern, text_lower).group(0))

        return keywords


def main():
    """Test document processor"""
    # Use default config (loads from settings.yaml)
    processor = DocumentProcessor()

    # Load documents
    docs_dir = "../../data/documents"
    docs = processor.load_documents(docs_dir)

    # Chunk documents
    chunks = processor.chunk_documents(docs)

    # Add metadata
    chunks = processor.extract_metadata(chunks)

    # Print sample
    print(f"\nSample chunk:")
    print(f"Source: {chunks[0]['source']}")
    print(f"Text: {chunks[0]['text'][:200]}...")
    print(f"Keywords: {chunks[0]['keywords']}")
    print(f"Has steps: {chunks[0]['has_steps']}")


if __name__ == "__main__":
    main()
