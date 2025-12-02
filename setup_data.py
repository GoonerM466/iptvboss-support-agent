"""
Setup Script - Copy documents and images from RAG Docs to data directory
"""

import shutil
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def setup_data_directory():
    """Copy documents and images to data directory"""

    project_root = Path(__file__).parent
    source_base = project_root.parent / "RAG Docs"
    dest_base = project_root / "data"

    logger.info("=" * 60)
    logger.info("IPTVBoss Support Agent - Data Setup")
    logger.info("=" * 60)

    # Check if source exists
    if not source_base.exists():
        logger.error(f"❌ Source directory not found: {source_base}")
        logger.info("Please ensure 'RAG Docs' folder exists")
        return False

    # Create destination directories
    docs_dest = dest_base / "documents"
    images_dest = dest_base / "images"

    docs_dest.mkdir(parents=True, exist_ok=True)
    images_dest.mkdir(parents=True, exist_ok=True)

    # Copy documentation files
    logger.info("\n[1/2] Copying documentation files...")

    doc_sources = [
        source_base / "documentation",
        source_base / "references"
    ]

    total_docs = 0
    for source_dir in doc_sources:
        if source_dir.exists():
            for md_file in source_dir.glob("*.md"):
                dest_file = docs_dest / md_file.name
                shutil.copy2(md_file, dest_file)
                logger.info(f"  ✓ Copied: {md_file.name}")
                total_docs += 1

    # Copy images
    logger.info("\n[2/2] Copying images...")

    images_source = source_base / "images"
    if images_source.exists():
        total_images = 0
        for img_file in images_source.glob("*.png"):
            dest_file = images_dest / img_file.name
            shutil.copy2(img_file, dest_file)
            total_images += 1

        logger.info(f"  ✓ Copied {total_images} images")
    else:
        logger.warning(f"  ⚠️  Images directory not found: {images_source}")

    # Summary
    logger.info("\n" + "=" * 60)
    logger.info("✅ Data setup complete!")
    logger.info(f"📄 Documents: {total_docs} files in {docs_dest}")
    logger.info(f"🖼️  Images: {total_images} files in {images_dest}")
    logger.info("\n📋 Next step: Run `python src/embeddings/build_vector_db.py`")
    logger.info("=" * 60)

    return True


if __name__ == "__main__":
    success = setup_data_directory()
    if not success:
        exit(1)
