"""
IPTVBoss Support Agent - Main Streamlit Application
"""

import os
import sys
from pathlib import Path
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import yaml

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from retrieval.vector_search import VectorSearch
from llm.gemini_client import GeminiClient
from ui.image_handler import ImageHandler
from conversation_state import SessionManager
from abuse_detection import AbuseHandler


def copy_button(text, button_id):
    """Add a copy-to-clipboard button using JavaScript"""
    # Escape text for JavaScript
    escaped_text = text.replace('\\', '\\\\').replace('`', '\\`').replace('$', '\\$')

    button_html = f"""
    <div style="margin: 10px 0;">
        <button onclick="copyToClipboard_{button_id}()" id="btn_{button_id}"
                style="background-color: #4CAF50; color: white; padding: 8px 16px;
                       border: none; border-radius: 4px; cursor: pointer; font-size: 14px;">
            📋 Copy Response
        </button>
    </div>
    <script>
        function copyToClipboard_{button_id}() {{
            const text = `{escaped_text}`;
            navigator.clipboard.writeText(text).then(function() {{
                const btn = document.getElementById('btn_{button_id}');
                btn.textContent = '✓ Copied!';
                btn.style.backgroundColor = '#45a049';
                setTimeout(function() {{
                    btn.textContent = '📋 Copy Response';
                    btn.style.backgroundColor = '#4CAF50';
                }}, 2000);
            }}).catch(function(err) {{
                console.error('Failed to copy: ', err);
            }});
        }}
    </script>
    """
    components.html(button_html, height=60)



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

    if 'session_manager' not in st.session_state:
        st.session_state.session_manager = SessionManager()

    if 'abuse_handler' not in st.session_state:
        st.session_state.abuse_handler = AbuseHandler()

    # Generate unique session ID for this Streamlit session
    if 'session_id' not in st.session_state:
        import uuid
        st.session_state.session_id = str(uuid.uuid4())

    # Track if conversation is terminated
    if 'conversation_terminated' not in st.session_state:
        st.session_state.conversation_terminated = False


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
            settings_path = project_root / "config" / "settings.yaml"
            image_map_path = project_root / "config" / "image_map.json"
            images_dir = project_root / "data" / "images"

            # Load settings
            with open(settings_path, 'r') as f:
                st.session_state.settings = yaml.safe_load(f)

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

        # Get default from settings
        default_min_score = st.session_state.get('settings', {}).get('vector_search', {}).get('min_score', 0.30)
        st.session_state.min_score = st.slider(
            "Search confidence threshold",
            min_value=0.0,
            max_value=1.0,
            value=default_min_score,
            step=0.01
        )


def determine_top_k(query: str, settings: dict) -> int:
    """Determine how many chunks to retrieve based on query type"""
    query_lower = query.lower()

    # Diagnostic/troubleshooting queries - fewer chunks, more focused
    diagnostic_keywords = [
        "not working", "doesn't work", "don't work", "broken", "error",
        "no data", "missing", "can't", "won't", "failed", "failure",
        "issue", "problem", "help", "stuck"
    ]
    if any(kw in query_lower for kw in diagnostic_keywords):
        return settings.get('vector_search', {}).get('top_k_diagnostic', 3)

    # How-to queries - moderate chunks
    if query_lower.startswith(("how do i", "how to", "how can", "how do you")):
        return settings.get('vector_search', {}).get('top_k_howto', 4)

    # General questions - standard chunks
    return settings.get('vector_search', {}).get('top_k_default', 5)


def handle_user_input(user_question: str):
    """Process user question and generate response"""
    # Check if conversation is terminated
    if st.session_state.get('conversation_terminated', False):
        with st.chat_message("model"):
            st.error("This conversation has been terminated. Please refresh the page to start over, or visit Discord for support.")
        return

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.chat_message("user"):
        st.write(user_question)

    # Check for abuse/aggression
    user_id = st.session_state.get('session_id', 'default_user')
    abuse_handler = st.session_state.abuse_handler
    should_continue, abuse_response, cleaned_message = abuse_handler.handle_message(user_id, user_question)

    if abuse_response:
        # User received warning or shutdown
        st.session_state.messages.append({
            "role": "model",
            "content": abuse_response
        })

        with st.chat_message("model"):
            if should_continue:
                st.warning(abuse_response)
                # IMPORTANT: Don't return - continue processing cleaned message
            else:
                # Terminate conversation
                st.session_state.conversation_terminated = True
                st.error(abuse_response)
                return  # Only return on shutdown

    # Use cleaned message for processing (removes aggressive language but keeps actual question)
    user_question = cleaned_message

    # Check for sensitive information
    gemini_client = st.session_state.gemini_client
    if gemini_client.detect_sensitive_request(user_question):
        warning_msg = gemini_client.get_sensitive_warning()
        st.session_state.messages.append({
            "role": "model",
            "content": warning_msg
        })

        with st.chat_message("model"):
            st.warning(warning_msg)
        return

    # Generate response
    with st.chat_message("model"):
        with st.spinner("Searching knowledge base..."):
            # Get user session for state tracking
            user_id = st.session_state.get('session_id', 'default_user')
            session = st.session_state.session_manager.get_session(user_id)

            # Parse user message for signals (tried X, it worked, etc.)
            parsed = session.parse_user_message(user_question)

            # Update session based on parsed info
            if parsed['tried_solution']:
                session.add_attempted_solution(parsed['solution_name'])
                if parsed['solution_worked'] == True:
                    # Problem solved - reset session
                    st.session_state.session_manager.clear_session(user_id)

            # Vector search with adaptive top_k
            vector_search = st.session_state.vector_search
            settings = st.session_state.get('settings', {})

            # Use settings.yaml values
            default_min_score = settings.get('vector_search', {}).get('min_score', 0.30)
            min_score = st.session_state.get('min_score', default_min_score)

            # Augment query with conversation context if too short/vague
            search_query = user_question
            if len(user_question.split()) < 5 and len(st.session_state.messages) > 2:
                # Query is short - add context from recent messages
                recent_user_messages = [
                    msg['content'] for msg in st.session_state.messages[-6:]
                    if msg['role'] == 'user'
                ]
                if recent_user_messages:
                    # Combine recent context with current query
                    context_keywords = ' '.join(recent_user_messages[-2:])  # Last 2 user messages
                    search_query = f"{user_question} {context_keywords}"

            # Determine top_k based on query type
            top_k = determine_top_k(search_query, settings)

            context, retrieved_chunks = vector_search.search_with_context(
                search_query,
                top_k=top_k,
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

            # Generate answer with conversation state
            conversation_history = [
                msg for msg in st.session_state.messages[-6:]
                if msg['role'] in ['user', 'model']
            ]

            # Get session context for LLM
            session_context = session.get_context_for_llm()

            # Add emotional context if user is frustrated
            emotional_note = abuse_handler.get_context_note(user_id, user_question)
            if emotional_note:
                session_context = f"{session_context}\n\n{emotional_note}"

            answer = gemini_client.generate_answer(
                user_question,
                context,
                conversation_history,
                conversation_state=session_context
            )

            # Display answer (may contain embedded images via markdown)
            st.write(answer)

            # Add copy button for the response
            copy_button(answer, f"new_{hash(answer)}")

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
                "role": "model",
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

            # Add copy button for model messages in history
            if role == "model":
                copy_button(content, f"history_{hash(content)}")

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
            "role": "model",
            "content": greeting
        })

    render_chat()


if __name__ == "__main__":
    main()
