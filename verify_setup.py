"""
Setup Verification Script - Check if everything is ready
"""

import sys
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def print_header(text):
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)


def check_python():
    """Check Python version"""
    version = sys.version_info
    if version < (3, 9):
        logger.error(f"❌ Python 3.9+ required (found {version.major}.{version.minor})")
        return False
    logger.info(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True


def check_dependencies():
    """Check if required packages are installed"""
    required = [
        'streamlit',
        'faiss',
        'sentence_transformers',
        'google.generativeai',
        'yaml',
        'PIL'
    ]

    missing = []
    installed = []

    for package in required:
        try:
            __import__(package)
            installed.append(package)
        except ImportError:
            missing.append(package)

    if installed:
        logger.info(f"✅ Installed packages: {', '.join(installed)}")

    if missing:
        logger.warning(f"⚠️  Missing packages: {', '.join(missing)}")
        logger.info("\nInstall with:")
        logger.info("  pip install -r deployment/requirements.txt")
        return False

    logger.info("✅ All dependencies installed")
    return True


def check_data():
    """Check if data files exist"""
    data_dir = Path("data")
    docs_dir = data_dir / "documents"
    images_dir = data_dir / "images"

    checks = {
        "Documents directory": docs_dir.exists(),
        "Images directory": images_dir.exists(),
    }

    if docs_dir.exists():
        doc_count = len(list(docs_dir.glob("*.md")))
        checks[f"  - Document files ({doc_count} found)"] = doc_count >= 6

    if images_dir.exists():
        img_count = len(list(images_dir.glob("*.png")))
        checks[f"  - Image files ({img_count} found)"] = img_count >= 40

    all_ok = True
    for check, result in checks.items():
        if result:
            logger.info(f"✅ {check}")
        else:
            logger.error(f"❌ {check}")
            all_ok = False

    if not all_ok:
        logger.info("\nRun data setup:")
        logger.info("  python setup_data.py")
        return False

    return True


def check_vector_db():
    """Check if vector database exists"""
    vector_db_dir = Path("data/vector_db")
    index_file = vector_db_dir / "faiss_index.bin"
    chunks_file = vector_db_dir / "chunks_metadata.pkl"

    if index_file.exists() and chunks_file.exists():
        logger.info("✅ Vector database built")
        return True
    else:
        logger.warning("⚠️  Vector database not built")
        logger.info("\nBuild vector database:")
        logger.info("  python src/embeddings/build_vector_db.py")
        return False


def check_config():
    """Check if configuration files exist"""
    checks = {
        "prompts.yaml": Path("config/prompts.yaml").exists(),
        "image_map.json": Path("config/image_map.json").exists(),
        "settings.yaml": Path("config/settings.yaml").exists(),
        ".streamlit/config.toml": Path(".streamlit/config.toml").exists(),
    }

    all_ok = True
    for file, exists in checks.items():
        if exists:
            logger.info(f"✅ {file}")
        else:
            logger.error(f"❌ {file} missing")
            all_ok = False

    return all_ok


def check_api_key():
    """Check if Gemini API key is configured"""
    import os

    # Check environment variable
    if os.getenv('GEMINI_API_KEY'):
        logger.info("✅ GEMINI_API_KEY (environment variable)")
        return True

    # Check secrets file
    secrets_file = Path(".streamlit/secrets.toml")
    if secrets_file.exists():
        content = secrets_file.read_text()
        if 'GEMINI_API_KEY' in content and 'your-api-key-here' not in content.lower():
            logger.info("✅ GEMINI_API_KEY (secrets.toml)")
            return True

    logger.warning("⚠️  GEMINI_API_KEY not configured")
    logger.info("\nGet API key from: https://aistudio.google.com/app/apikey")
    logger.info("Then create .streamlit/secrets.toml:")
    logger.info('  GEMINI_API_KEY = "your-key-here"')
    return False


def main():
    """Run all checks"""
    print_header("IPTVBoss Support Agent - Setup Verification")

    checks = [
        ("Python Version", check_python),
        ("Dependencies", check_dependencies),
        ("Data Files", check_data),
        ("Vector Database", check_vector_db),
        ("Configuration", check_config),
        ("API Key", check_api_key),
    ]

    results = []
    for name, check_func in checks:
        print(f"\n📋 Checking {name}...")
        print("-" * 60)
        results.append((name, check_func()))

    # Summary
    print_header("Verification Summary")

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")

    print(f"\nScore: {passed}/{total}")

    if passed == total:
        print("\n🎉 All checks passed! Ready to run:")
        print("   streamlit run app.py")
    else:
        print("\n⚠️  Some checks failed. Follow instructions above to fix.")
        print("\nQuick fix for common issues:")
        print("1. Install dependencies: pip install -r deployment/requirements.txt")
        print("2. Copy data: python setup_data.py")
        print("3. Build DB: python src/embeddings/build_vector_db.py")
        print("4. Configure API key: Edit .streamlit/secrets.toml")

    print("=" * 60)

    return passed == total


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Verification failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
