"""
IPTVBoss Support Agent - Main Streamlit Application
"""

import os
import sys
from pathlib import Path
import streamlit as st
from PIL import Image
from streamlit_extras.copy_button import copy_button

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from retrieval.vector_search import VectorSearch
from llm.gemini_client import GeminiClient
from ui.image_handler import ImageHandler


# Page configuration
st.set_page_config(
    page_title="IPTVBoss QSA",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subheader {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .warning-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 4px;
    }
    .info-box {
        background-color: #d1ecf1;
        border-left: 4px solid #17a2b8;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 4px;
    }
    .image-caption {
        text-align: center;
        color: #666;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize Streamlit session state"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if 'initialized' not in st.session_state:
        st.session_state.initialized = False


def load_components():
    """Load RAG components (cached)"""
    if st.session_state.initialized:
        return

    with st.spinner("Initializing support agent..."):
        try:
            # Paths
            project_root = Path(__file__).parent
            vector_db_path = project_root / "data" / "vector_db"
            prompts_path = project_root / "config" / "prompts.yaml"
            image_map_path = project_root / "config" / "image_map.json"
            images_dir = project_root / "data" / "images"

            # Get Gemini API key
            gemini_api_key = os.getenv('GEMINI_API_KEY') or st.secrets.get("GEMINI_API_KEY")

            if not gemini_api_key:
                st.error("❌ GEMINI_API_KEY not configured. Please set in .streamlit/secrets.toml")
                st.stop()

            # Initialize components
            st.session_state.vector_search = VectorSearch(str(vector_db_path))
            st.session_state.gemini_client = GeminiClient(
                gemini_api_key,
                str(prompts_path)
            )
            st.session_state.image_handler = ImageHandler(
                str(image_map_path),
                str(images_dir)
            )

            st.session_state.initialized = True

        except FileNotFoundError as e:
            st.error(f"❌ Required file not found: {e}")
            st.info("📋 Please run: `python src/embeddings/build_vector_db.py` first")
            st.stop()
        except Exception as e:
            st.error(f"❌ Initialization error: {e}")
            st.stop()


def render_header():
    """Render page header"""
    st.markdown('<div class="main-header">🎬 IPTVBoss Quick Support Agent</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subheader">AI-powered support for IPTVBoss & EPGBoss</div>',
        unsafe_allow_html=True
    )

    # Privacy warning
    st.markdown("""
    <div class="warning-box">
        ⚠️ <strong>Privacy Reminder:</strong> Never share passwords, provider URLs, API keys, or credentials with this agent.
    </div>
    """, unsafe_allow_html=True)


def render_sidebar():
    """Render sidebar with info and settings"""
    with st.sidebar:
        st.header("ℹ️ About")

        st.markdown("""
        This AI agent can help you with:
        - Setting up IPTVBoss
        - Understanding features
        - Troubleshooting issues
        - Finding documentation

        **It cannot:**
        - Access your system
        - Modify your files
        - Help with account/billing
        - Supply provider credentials or links
        """)

        st.divider()

        st.header("📚 Resources")
        st.markdown("""
        - [Discord Support](https://discord.gg/QCxpA9yvWP)
        - [Official Website](https://members.bosstees.net)
        - [User Guide](https://goonerm466.github.io/iptvboss-support-agent/)
        """)

        st.divider()

        st.header("💡 Example Questions")
        examples = [
            "How do I set up Dropbox?",
            "My EPG isn't showing",
            "What's the difference between M3U and XC?",
            "How do I create a layout?"
        ]

        for example in examples:
            if st.button(example, key=f"example_{example}"):
                st.session_state.selected_example = example

        st.divider()

        # Settings
        st.header("⚙️ Settings")
        st.session_state.show_debug = st.checkbox("Show debug info", value=False)
        st.session_state.min_score = st.slider(
            "Search confidence threshold",
            min_value=0.0,
            max_value=1.0,
            value=0.35,
            step=0.05
        )


def handle_user_input(user_question: str):
    """Process user question and generate response"""
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.chat_message("user"):
        st.write(user_question)

    # Check for sensitive information
    gemini_client = st.session_state.gemini_client
    if gemini_client.detect_sensitive_request(user_question):
        warning_msg = gemini_client.get_sensitive_warning()
        st.session_state.messages.append({
            "role": "assistant",
            "content": warning_msg
        })

        with st.chat_message("assistant"):
            st.warning(warning_msg)
        return

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base..."):
            # Vector search
            vector_search = st.session_state.vector_search
            min_score = st.session_state.get('min_score', 0.2)  # Updated default

            context, retrieved_chunks = vector_search.search_with_context(
                user_question,
                top_k=10,  # INCREASED from 3 for better context coverage
                min_score=min_score
            )

            # Debug info
            if st.session_state.get('show_debug', False):
                with st.expander("🔍 Debug: Retrieved Chunks"):
                    for i, chunk in enumerate(retrieved_chunks, 1):
                        st.write(f"**Chunk {i}** (score: {chunk['score']:.3f})")
                        st.write(f"Source: `{chunk['source']}`")
                        st.write(chunk['text'][:300] + "...")
                        st.divider()

            # Generate answer
            conversation_history = [
                msg for msg in st.session_state.messages[-6:]
                if msg['role'] in ['user', 'model']
            ]

            answer = gemini_client.generate_answer(
                user_question,
                context,
                conversation_history
            )

            # Display answer (may contain embedded images via markdown)
            st.write(answer)

            # Add copy button for the response
            copy_button(answer, "📋 Copy Response")

            # Detect and display relevant images that weren't already embedded
            image_handler = st.session_state.image_handler
            relevant_images = image_handler.detect_relevant_images(
                user_question,
                retrieved_chunks,
                max_images=3
            )

            # Also check if answer mentions specific images
            image_refs = image_handler.extract_image_refs_from_answer(answer)
            for ref in image_refs:
                img_info = image_handler.get_image_by_name(ref)
                if img_info and img_info not in relevant_images:
                    relevant_images.append(img_info)

            # Extract embedded images from answer to avoid duplication
            import re
            embedded_pattern = r'!\[.*?\]\(.*?/images/(image\d+\.png)\)'
            embedded_images = re.findall(embedded_pattern, answer)

            # Filter out images that were already embedded in the response
            images_to_display = [
                img for img in relevant_images
                if img['path'].split('/')[-1] not in embedded_images and
                   img['path'].split('\\')[-1] not in embedded_images
            ]

            # Display additional relevant images (not already embedded)
            if images_to_display:
                st.markdown("---")
                st.markdown("**📷 Additional Relevant Images:**")

                # Display in columns
                cols = st.columns(min(len(images_to_display), 3))

                for i, img_info in enumerate(images_to_display[:3]):
                    with cols[i]:
                        try:
                            img = Image.open(img_info['path'])
                            st.image(img, width='stretch')
                            st.markdown(
                                f'<div class="image-caption">{img_info["description"]}</div>',
                                unsafe_allow_html=True
                            )
                        except Exception as e:
                            st.error(f"Error loading image: {e}")

            # Add to message history (store only additional images, not embedded ones)
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "images": images_to_display
            })


def render_chat():
    """Render chat interface"""
    # Display chat history
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]

        with st.chat_message(role):
            st.write(content)

            # Add copy button for assistant messages in history
            if role == "assistant":
                copy_button(content, "📋 Copy Response", key=f"copy_history_{len(st.session_state.messages)}_{hash(content)}")

            # Display additional images if present (not embedded in content)
            if "images" in message and message["images"]:
                st.markdown("---")
                st.markdown("**📷 Additional Relevant Images:**")

                cols = st.columns(min(len(message["images"]), 3))
                for i, img_info in enumerate(message["images"][:3]):
                    with cols[i]:
                        try:
                            img = Image.open(img_info['path'])
                            st.image(img, width='stretch')
                            st.markdown(
                                f'<div class="image-caption">{img_info["description"]}</div>',
                                unsafe_allow_html=True
                            )
                        except:
                            pass

    # Chat input
    if prompt := st.chat_input("Ask me anything about IPTVBoss..."):
        handle_user_input(prompt)

    # Handle example button clicks
    if 'selected_example' in st.session_state:
        example = st.session_state.selected_example
        del st.session_state.selected_example
        handle_user_input(example)


def main():
    """Main application"""
    initialize_session_state()
    load_components()
    render_header()
    render_sidebar()

    # Show greeting if first visit
    if not st.session_state.messages:
        greeting = st.session_state.gemini_client.get_greeting()
        st.session_state.messages.append({
            "role": "assistant",
            "content": greeting
        })

    render_chat()


if __name__ == "__main__":
    main()
