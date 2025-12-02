"""
Image Handler - Detect topics and display relevant images
"""

import json
import logging
from pathlib import Path
from typing import List, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ImageHandler:
    """Handle image mapping and conditional display"""

    def __init__(self, image_map_path: str, images_dir: str):
        """
        Args:
            image_map_path: Path to image_map.json
            images_dir: Path to directory containing image files
        """
        self.images_dir = Path(images_dir)

        # Load image mapping
        with open(image_map_path, 'r', encoding='utf-8') as f:
            self.image_map = json.load(f)

        logger.info(f"Loaded image map with {len(self.image_map['mappings'])} categories")

    def detect_relevant_images(
        self,
        question: str,
        retrieved_chunks: List[Dict],
        max_images: int = 3
    ) -> List[Dict[str, str]]:
        """
        Detect which images are relevant to the question and context

        Args:
            question: User's question
            retrieved_chunks: Retrieved context chunks from vector search
            max_images: Maximum number of images to return

        Returns:
            List of dicts with 'filename', 'description', and 'path' keys
        """
        # Get which source files were retrieved
        source_files = set()
        for chunk in retrieved_chunks:
            source = chunk.get('source', '')
            if source:
                # Extract just the filename from the path
                source_filename = Path(source).name
                source_files.add(source_filename)

        logger.debug(f"Retrieved source files: {source_files}")

        # Combine question and retrieved text for matching
        combined_text = question.lower()

        for chunk in retrieved_chunks:
            combined_text += " " + chunk.get('text', '').lower()

        # Score each mapping
        scored_mappings = []

        for mapping in self.image_map['mappings']:
            score = 0

            # Check if mapping has source_files restriction
            if 'source_files' in mapping:
                # Only consider this mapping if at least one of its source files was retrieved
                mapping_sources = set(mapping['source_files'])
                if not mapping_sources.intersection(source_files):
                    # No matching source files retrieved, skip this mapping
                    continue

            # Check keyword matches
            for keyword in mapping['keywords']:
                if keyword.lower() in combined_text:
                    score += 1

            if score > 0:
                scored_mappings.append({
                    'mapping': mapping,
                    'score': score
                })

        # Sort by score
        scored_mappings.sort(key=lambda x: x['score'], reverse=True)

        # Build results
        results = []
        seen_images = set()

        for item in scored_mappings[:max_images]:
            mapping = item['mapping']

            # Get images (take first one or two from each mapping)
            for image_file in mapping['images'][:2]:
                if image_file in seen_images:
                    continue

                seen_images.add(image_file)
                image_path = self.images_dir / image_file

                if image_path.exists():
                    results.append({
                        'filename': image_file,
                        'description': self.image_map['image_details'].get(
                            image_file,
                            mapping['description']
                        ),
                        'path': str(image_path)
                    })

                if len(results) >= max_images:
                    break

            if len(results) >= max_images:
                break

        logger.debug(f"Detected {len(results)} relevant images for question")
        return results

    def get_image_by_name(self, filename: str) -> Optional[Dict[str, str]]:
        """
        Get image info by filename

        Args:
            filename: Image filename (e.g., "image5.png")

        Returns:
            Dict with image info or None if not found
        """
        image_path = self.images_dir / filename

        if not image_path.exists():
            logger.warning(f"Image not found: {filename}")
            return None

        return {
            'filename': filename,
            'description': self.image_map['image_details'].get(filename, filename),
            'path': str(image_path)
        }

    def extract_image_refs_from_answer(self, answer: str) -> List[str]:
        """
        Extract image references from LLM answer (e.g., "See image5.png")

        Args:
            answer: Generated answer text

        Returns:
            List of image filenames mentioned in answer
        """
        import re

        # Pattern: imageXX.png or image XX
        pattern = r'image\s*(\d+)(?:\.png)?'
        matches = re.findall(pattern, answer, re.IGNORECASE)

        # Convert to standard format
        image_refs = [f"image{num}.png" for num in matches]

        logger.debug(f"Extracted {len(image_refs)} image references from answer")
        return image_refs


def main():
    """Test image handler"""
    from pathlib import Path

    project_root = Path(__file__).parent.parent.parent
    image_map_path = project_root / "config" / "image_map.json"
    images_dir = project_root / "data" / "images"

    if not image_map_path.exists():
        print(f"ERROR: Image map not found: {image_map_path}")
        return

    handler = ImageHandler(str(image_map_path), str(images_dir))

    # Test queries
    test_cases = [
        {
            "question": "How do I set up Dropbox?",
            "chunks": [{"text": "Dropbox setup requires creating an app..."}]
        },
        {
            "question": "My EPG isn't showing",
            "chunks": [{"text": "EPG layout settings can be customized..."}]
        },
        {
            "question": "How do I use the Layout Editor?",
            "chunks": [{"text": "The Layout Editor interface allows..."}]
        }
    ]

    print("\n" + "=" * 60)
    print("Image Handler Test")
    print("=" * 60)

    for case in test_cases:
        print(f"\nQuestion: {case['question']}")
        print("-" * 60)

        images = handler.detect_relevant_images(
            case['question'],
            case['chunks'],
            max_images=3
        )

        if images:
            print(f"Relevant images ({len(images)}):")
            for img in images:
                print(f"  - {img['filename']}: {img['description']}")
        else:
            print("  No relevant images found")


if __name__ == "__main__":
    main()
