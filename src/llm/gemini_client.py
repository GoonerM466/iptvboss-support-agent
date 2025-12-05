"""
Gemini API Client - LLM integration with anti-hallucination safeguards
"""

import os
import logging
from typing import Dict, List, Optional
import yaml
from pathlib import Path

try:
    import google.generativeai as genai
except ImportError:
    print("ERROR: google-generativeai not installed")
    print("Run: pip install google-generativeai")
    raise

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GeminiClient:
    """Client for Google Gemini API with RAG support"""

    def __init__(
        self,
        api_key: str,
        prompts_config_path: Optional[str] = None,
        settings_config_path: Optional[str] = None
    ):
        """
        Args:
            api_key: Gemini API key
            prompts_config_path: Path to prompts.yaml file
            settings_config_path: Path to settings.yaml (optional, defaults to config/settings.yaml)
        """
        # Configure Gemini
        genai.configure(api_key=api_key)

        # Load settings from YAML
        if settings_config_path is None:
            settings_config_path = Path(__file__).parent.parent.parent / "config" / "settings.yaml"

        with open(settings_config_path, 'r', encoding='utf-8') as f:
            settings = yaml.safe_load(f)

        # Extract LLM settings
        llm_config = settings['llm']
        self.model_name = llm_config.get('model', 'gemini-2.5-flash')
        self.temperature = llm_config.get('temperature', 0.4)
        self.top_p = llm_config.get('top_p', 0.8)
        self.top_k = llm_config.get('top_k', 40)
        self.max_output_tokens = llm_config.get('max_output_tokens', 10000)

        # Load prompts
        if prompts_config_path:
            with open(prompts_config_path, 'r', encoding='utf-8') as f:
                self.prompts = yaml.safe_load(f)
        else:
            # Default prompts
            self.prompts = self._default_prompts()

        # Initialize model with safety settings
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=self._generation_config(),
            safety_settings=self._safety_settings()
        )

        logger.info(f"Initialized Gemini client with model: {self.model_name}")
        logger.info(f"  temperature: {self.temperature}")
        logger.info(f"  top_p: {self.top_p}")
        logger.info(f"  top_k: {self.top_k}")
        logger.info(f"  max_output_tokens: {self.max_output_tokens}")

    def _generation_config(self) -> Dict:
        """Generation configuration for controlled output"""
        return {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "max_output_tokens": self.max_output_tokens,
        }

    def _safety_settings(self) -> List[Dict]:
        """Safety settings"""
        return [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        ]

    def _default_prompts(self) -> Dict:
        """Default prompts if config not loaded"""
        return {
            'system_prompt': "You are a helpful assistant. Answer only based on provided context.",
            'answer_prompt': "Context: {context}\n\nQuestion: {question}\n\nAnswer:",
            'no_context_response': "I don't have that information.",
            'greeting': "Hello! How can I help you?"
        }

    def generate_answer(
        self,
        question: str,
        context: str,
        conversation_history: Optional[List[Dict]] = None,
        conversation_state: str = ""
    ) -> str:
        """
        Generate answer using Gemini with strict context grounding

        Args:
            question: User's question
            context: Retrieved context from vector search
            conversation_history: Optional conversation history
            conversation_state: Conversation state context (what user has tried, etc.)

        Returns:
            Generated answer
        """
        # Build prompt
        system_prompt = self.prompts['system_prompt']
        answer_template = self.prompts['answer_prompt']

        # Get diagnostic instructions
        diagnostic_instructions = self.prompts.get('diagnostic_mode_instructions', '')

        # Format conversation state
        state_text = ""
        if conversation_state:
            state_text = f"\n### CONVERSATION STATE\n{conversation_state}\n"

        # Format with context
        user_prompt = answer_template.format(
            diagnostic_instructions=diagnostic_instructions,
            context=context if context else "No relevant context found.",
            conversation_state=state_text,
            question=question
        )

        # Build conversation
        messages = []

        # Add system prompt (as first user message for Gemini)
        messages.append({
            'role': 'user',
            'parts': [system_prompt]
        })
        messages.append({
            'role': 'model',
            'parts': ["Understood. I will answer only based on provided context."]
        })

        # Add conversation history if provided
        if conversation_history:
            for msg in conversation_history[-6:]:  # Last 3 exchanges
                messages.append({
                    'role': msg['role'],
                    'parts': [msg['content']]
                })

        # Add current question
        messages.append({
            'role': 'user',
            'parts': [user_prompt]
        })

        try:
            # Generate response
            # chat = self.model.start_chat(history=messages[:-1])
            response = self.model.generate_content(
                contents=messages
            )
            answer = response.text.strip()

            # Validate answer doesn't hallucinate
            if not context and "I don't have" not in answer:
                # No context but model gave substantive answer = hallucination
                logger.warning("Possible hallucination detected (no context)")
                answer = self.prompts['no_context_response']

            return answer

        except Exception as e:
            logger.error(f"Gemini API error: {e}")
            return "I'm having trouble generating a response. Please try again."

    def get_greeting(self) -> str:
        """Get greeting message"""
        return self.prompts.get('greeting', "Hello! How can I help you?")

    def get_no_context_response(self) -> str:
        """Get response for when no context is found"""
        return self.prompts.get('no_context_response', "I don't have that information.")

    def detect_sensitive_request(self, question: str) -> bool:
        """
        Detect if user is asking for or sharing sensitive information

        Args:
            question: User's question

        Returns:
            True if sensitive content detected
        """
        sensitive_keywords = [
            'password', 'credential', 'api key', 'token', 'secret',
            'username', 'login', 'my provider', 'provider url',
            'here is my log', 'here\'s my log', 'my log file'
        ]

        question_lower = question.lower()
        return any(keyword in question_lower for keyword in sensitive_keywords)

    def get_sensitive_warning(self) -> str:
        """Get warning message for sensitive information"""
        return self.prompts.get('sensitive_info_warning',
            "⚠️ Please don't share sensitive information with me.")


def main():
    """Test Gemini client"""
    import sys

    # Check for API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("ERROR: GEMINI_API_KEY environment variable not set")
        print("Get your key from: https://aistudio.google.com/app/apikey")
        sys.exit(1)

    # Load prompts
    project_root = Path(__file__).parent.parent.parent
    prompts_path = project_root / "config" / "prompts.yaml"

    # Initialize client
    client = GeminiClient(api_key, str(prompts_path))

    # Test query
    test_context = """
    To set up Dropbox with IPTVBoss:
    1. Go to https://www.dropbox.com/developers/apps
    2. Create a new app
    3. Select "Scoped access"
    4. Choose "Full Dropbox" access
    5. Set the required permissions
    """

    test_question = "How do I set up Dropbox?"

    print("\n" + "=" * 60)
    print("Gemini Client Test")
    print("=" * 60)
    print(f"\nQuestion: {test_question}")
    print("\nGenerating answer...")

    answer = client.generate_answer(test_question, test_context)

    print("\n" + "-" * 60)
    print("Answer:")
    print(answer)
    print("=" * 60)


if __name__ == "__main__":
    main()
