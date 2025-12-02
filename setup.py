"""
Complete Setup Script - One command to set up everything
"""

import os
import sys
import subprocess
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def print_header(text):
    """Print formatted header"""
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)


def print_step(step_num, total, text):
    """Print step header"""
    print(f"\n[{step_num}/{total}] {text}")
    print("-" * 60)


def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 9):
        logger.error("❌ Python 3.9 or higher required")
        logger.info(f"Current version: {sys.version}")
        return False
    logger.info(f"✅ Python {sys.version.split()[0]}")
    return True


def install_dependencies():
    """Install Python dependencies"""
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "deployment/requirements.txt"],
            check=True,
            capture_output=True
        )
        logger.info("✅ Dependencies installed")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Failed to install dependencies: {e}")
        return False


def setup_data():
    """Run data setup script"""
    try:
        subprocess.run(
            [sys.executable, "setup_data.py"],
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Data setup failed: {e}")
        return False


def build_vector_db():
    """Build vector database"""
    try:
        subprocess.run(
            [sys.executable, "src/embeddings/build_vector_db.py"],
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Vector DB build failed: {e}")
        return False


def check_api_key():
    """Check if Gemini API key is configured"""
    # Check environment variable
    if os.getenv('GEMINI_API_KEY'):
        logger.info("✅ GEMINI_API_KEY found in environment")
        return True

    # Check secrets file
    secrets_file = Path(".streamlit/secrets.toml")
    if secrets_file.exists():
        content = secrets_file.read_text()
        if 'GEMINI_API_KEY' in content and 'your-api-key-here' not in content:
            logger.info("✅ GEMINI_API_KEY found in secrets.toml")
            return True

    logger.warning("⚠️  GEMINI_API_KEY not configured")
    logger.info("\nTo configure:")
    logger.info("1. Get API key: https://aistudio.google.com/app/apikey")
    logger.info("2. Create .streamlit/secrets.toml:")
    logger.info('   GEMINI_API_KEY = "your-key-here"')
    logger.info("\nOr set environment variable:")
    logger.info('   export GEMINI_API_KEY="your-key-here"  # macOS/Linux')
    logger.info('   set GEMINI_API_KEY=your-key-here       # Windows')

    return False


def create_secrets_template():
    """Create secrets.toml template if it doesn't exist"""
    secrets_dir = Path(".streamlit")
    secrets_dir.mkdir(exist_ok=True)

    secrets_file = secrets_dir / "secrets.toml"
    if not secrets_file.exists():
        secrets_file.write_text(
            '# Google Gemini API Key\n'
            '# Get from: https://aistudio.google.com/app/apikey\n'
            'GEMINI_API_KEY = "your-api-key-here"\n'
        )
        logger.info(f"✅ Created {secrets_file}")


def main():
    """Run complete setup"""
    print_header("IPTVBoss Support Agent - Setup")

    # Step 1: Check Python version
    print_step(1, 6, "Checking Python version...")
    if not check_python_version():
        return False

    # Step 2: Install dependencies
    print_step(2, 6, "Installing dependencies...")
    if not install_dependencies():
        return False

    # Step 3: Setup data directory
    print_step(3, 6, "Setting up data directory...")
    if not setup_data():
        return False

    # Step 4: Build vector database
    print_step(4, 6, "Building vector database...")
    if not build_vector_db():
        return False

    # Step 5: Create secrets template
    print_step(5, 6, "Creating configuration files...")
    create_secrets_template()

    # Step 6: Check API key
    print_step(6, 6, "Checking Gemini API key...")
    api_key_configured = check_api_key()

    # Summary
    print_header("Setup Complete!")

    if api_key_configured:
        logger.info("✅ All steps completed successfully!")
        logger.info("\n📋 Next steps:")
        logger.info("1. Run: streamlit run app.py")
        logger.info("2. Visit: http://localhost:8501")
        logger.info("3. Test with sample queries")
        logger.info("\n📚 See QUICKSTART.md for deployment instructions")
    else:
        logger.warning("⚠️  Setup complete but API key not configured")
        logger.info("\n📋 Next steps:")
        logger.info("1. Configure GEMINI_API_KEY (see instructions above)")
        logger.info("2. Run: streamlit run app.py")
        logger.info("3. Visit: http://localhost:8501")

    print("=" * 60)
    return True


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Setup failed: {e}")
        sys.exit(1)
