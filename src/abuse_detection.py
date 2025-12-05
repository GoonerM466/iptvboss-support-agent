"""
Abuse Detection - Handle user frustration and aggression with nuanced responses
"""

from typing import Dict, Tuple, Optional
import re


class AbuseDetector:
    """Detect and categorize user frustration vs. aggression"""

    def __init__(self):
        # Contextual swearing (frustration at situation, not at agent)
        self.frustration_words = [
            "damn", "dammit", "crap", "shit", "fuck", "fucking",
            "hell", "bloody", "wtf", "ffs"
        ]

        # Words directed at agent (aggression)
        self.aggression_patterns = [
            r"\b(you'?re? (?:useless|stupid|dumb|worthless|terrible|garbage|shit|fucking useless))",
            r"\b(stupid (?:bot|agent|ai))",
            r"\b(fuck you|screw you)",
            r"\b(shut up|shut the fuck up)",
            r"\b(you (?:suck|don'?t know (?:shit|anything)))",
            r"\b(this (?:bot|agent|ai) is (?:useless|garbage|shit|terrible))",
            r"\b(waste of (?:time|my time))",
            r"\b(you'?re? (?:not helping|no help))",
        ]

        # Extreme aggression (immediate shutdown)
        self.extreme_patterns = [
            r"(?:fuck|screw|damn) (?:you|this bot|this agent)",
            r"you'?re? (?:a )?(?:fucking )?(?:piece of shit|worthless|useless piece)",
            r"(?:stupid|dumb|useless) (?:fucking )?(?:bot|ai|agent)",
        ]

    def analyze_message(self, message: str) -> Dict:
        """
        Analyze message for frustration vs aggression

        Returns:
            {
                'level': 'none' | 'frustration' | 'mild_aggression' | 'aggression' | 'extreme',
                'aggressive_word_count': int,
                'is_directed_at_agent': bool,
                'examples': list of detected phrases
            }
        """
        message_lower = message.lower()

        # Count frustration words (contextual swearing)
        frustration_count = sum(
            1 for word in self.frustration_words
            if word in message_lower
        )

        # Check for aggression patterns
        aggression_matches = []
        for pattern in self.aggression_patterns:
            matches = re.findall(pattern, message_lower)
            aggression_matches.extend(matches)

        # Check for extreme aggression
        extreme_matches = []
        for pattern in self.extreme_patterns:
            matches = re.findall(pattern, message_lower)
            extreme_matches.extend(matches)

        # Determine level
        aggressive_word_count = len(aggression_matches)
        is_directed = len(aggression_matches) > 0 or len(extreme_matches) > 0

        if len(extreme_matches) > 0 or aggressive_word_count >= 5:
            level = 'extreme'
        elif aggressive_word_count >= 3:
            level = 'aggression'
        elif aggressive_word_count >= 1:
            level = 'mild_aggression'
        elif frustration_count > 0:
            level = 'frustration'
        else:
            level = 'none'

        return {
            'level': level,
            'aggressive_word_count': aggressive_word_count,
            'is_directed_at_agent': is_directed,
            'examples': aggression_matches + extreme_matches
        }


class AbuseHandler:
    """Handle user aggression with escalating responses"""

    def __init__(self):
        self.detector = AbuseDetector()
        self.user_warnings: Dict[str, int] = {}  # user_id -> warning count

    def handle_message(self, user_id: str, message: str) -> Tuple[bool, Optional[str], str]:
        """
        Check message for abuse and return appropriate response

        Returns:
            (should_continue, warning_message, cleaned_message)
            - should_continue: False if conversation should be terminated
            - warning_message: None if ok, warning/shutdown message if needed
            - cleaned_message: Message with abuse removed for processing
        """
        analysis = self.detector.analyze_message(message)
        level = analysis['level']

        # No issue - proceed normally
        if level == 'none':
            return (True, None, message)

        # Frustration (not directed at agent) - acknowledge and continue
        if level == 'frustration':
            # Don't warn, just note it in context, pass through original message
            return (True, None, message)

        # Extreme aggression - immediate shutdown
        if level == 'extreme':
            return (False, self._get_shutdown_response(), message)

        # Mild to moderate aggression - escalating warnings
        if level in ['mild_aggression', 'aggression']:
            warning_count = self.user_warnings.get(user_id, 0)
            warning_count += 1
            self.user_warnings[user_id] = warning_count

            # Clean the message by removing aggressive parts
            cleaned = self._clean_message(message, analysis['examples'])

            if warning_count >= 3:
                # Third strike - shutdown
                return (False, self._get_shutdown_response(), cleaned)
            else:
                # First or second warning - but still process cleaned message
                return (True, self._get_warning_response(warning_count), cleaned)

        return (True, None, message)

    def _clean_message(self, message: str, aggressive_phrases: list) -> str:
        """Remove aggressive phrases from message to extract actual question"""
        cleaned = message
        for phrase in aggressive_phrases:
            # Remove the aggressive phrase but keep the rest
            cleaned = re.sub(rf'\b{re.escape(phrase)}\b', '', cleaned, flags=re.IGNORECASE)

        # Clean up extra whitespace
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()

        # If message is now too short, return something neutral
        if len(cleaned) < 5:
            return "still not working"

        return cleaned

    def reset_warnings(self, user_id: str):
        """Reset warning count for user"""
        if user_id in self.user_warnings:
            del self.user_warnings[user_id]

    def _get_warning_response(self, warning_count: int) -> str:
        """Get varied warning messages"""
        warnings = [
            # First warning variants
            [
                "I understand this is frustrating, but I'm here to help. Getting angry at me won't solve the issue faster. Let's focus on finding a solution - being specific about what's happening helps me help you better.",

                "I get that you're frustrated with the situation, but taking it out on me doesn't help either of us. I have the knowledge to help you, but I need you to work with me. Let me know what's happening and we'll sort it out.",

                "Look, I'm trying to help you here, but directing anger at me isn't productive. I can solve this if you give me specific details about what's not working. Let's try to stay civil and fix your issue."
            ],
            # Second warning variants
            [
                "I've asked you to be civil. I'm still willing to help, but this is your second warning. If you continue being aggressive, I won't be able to assist further. Let's focus on solving your problem - tell me specifically what's not working.",

                "This is the second time I'm asking you to tone it down. I genuinely want to help you fix this, but I can't do that if you keep being hostile. One more aggressive message and I'll have to end this conversation. What specifically can I help you with?",

                "Second warning: I'm here to help, not to be your punching bag. I have all the information needed to solve your issue, but you need to communicate respectfully. This is your last chance - let's work together or I'll have to stop responding."
            ]
        ]

        # Return varied response based on warning count
        import random
        if warning_count == 1:
            return random.choice(warnings[0])
        else:  # warning_count == 2
            return random.choice(warnings[1])

    def _get_shutdown_response(self) -> str:
        """Get shutdown message (varied)"""
        import random
        shutdowns = [
            "I can't continue this conversation. Your behavior is unacceptable. If you need help, please refresh the page and start over with a respectful tone, or reach out on Discord where the team can assist you.",

            "This conversation is over. I'm not going to tolerate abusive behavior. If you genuinely need help with IPTVBoss, refresh the page and try again with civility, or ask politely on Discord.",

            "I'm ending this chat. Abusive language isn't acceptable. If you want technical support, refresh the page and communicate respectfully, or visit the Discord server and be polite to the support team there."
        ]
        return random.choice(shutdowns)

    def get_context_note(self, user_id: str, message: str) -> str:
        """Get context note for LLM about user's emotional state"""
        analysis = self.detector.analyze_message(message)
        level = analysis['level']
        warning_count = self.user_warnings.get(user_id, 0)

        if level == 'frustration':
            return "NOTE: User is frustrated with the situation (not you). Acknowledge their frustration empathetically while providing solution."
        elif level == 'mild_aggression' and warning_count == 1:
            return "NOTE: User received first warning for aggression. Be firm but still helpful."
        elif warning_count >= 2:
            return "NOTE: User received multiple warnings. Stay professional and focused on solution only."

        return ""
