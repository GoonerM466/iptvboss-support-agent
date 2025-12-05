"""
Conversation State Manager - Track diagnostic progress and conversation context
"""

from typing import List, Dict, Optional, Set
from datetime import datetime, timedelta
import re


class DiagnosticSession:
    """Manage diagnostic conversation state for a single user"""

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.flow_id: Optional[str] = None  # e.g., "no_data", "player_sync"
        self.confidence_level: str = "low"  # low, medium, high
        self.attempted_solutions: Set[str] = set()
        self.diagnostic_answers: Dict[str, str] = {}
        self.last_activity = datetime.now()
        self.conversation_history: List[Dict] = []
        self.questions_asked: int = 0

    def is_active(self, timeout_minutes: int = 15) -> bool:
        """Check if session is still active"""
        elapsed = datetime.now() - self.last_activity
        return elapsed < timedelta(minutes=timeout_minutes)

    def add_attempted_solution(self, solution_key: str):
        """Mark solution as tried"""
        self.attempted_solutions.add(solution_key.lower())
        self.last_activity = datetime.now()

    def record_answer(self, question: str, answer: str):
        """Record user's answer to diagnostic question"""
        self.diagnostic_answers[question] = answer
        self.last_activity = datetime.now()

    def update_confidence(self, level: str):
        """Update confidence level: low, medium, high"""
        if level in ["low", "medium", "high"]:
            self.confidence_level = level

    def increment_questions(self):
        """Increment count of questions asked"""
        self.questions_asked += 1

    def parse_user_message(self, message: str) -> Dict:
        """
        Parse user message for diagnostic signals

        Returns:
            {
                'tried_solution': bool,
                'solution_worked': Optional[bool],
                'solution_name': Optional[str]
            }
        """
        message_lower = message.lower()

        # Detect "I tried X"
        tried_patterns = [
            r"i tried (.+?)(?:\.|,|but|and|still|$)",
            r"i did (.+?)(?:\.|,|but|and|still|$)",
            r"already (.+?)(?:\.|,|but|and|still|$)",
            r"i've (.+?)(?:\.|,|but|and|still|$)",
            r"tried (.+?)(?:\.|,|but|and|still|$)"
        ]

        solution_name = None
        for pattern in tried_patterns:
            match = re.search(pattern, message_lower)
            if match:
                solution_name = match.group(1).strip()
                break

        # Detect success/failure
        success_keywords = ["worked", "fixed", "solved", "yes", "good", "success", "great", "that fixed", "now it works"]
        failure_keywords = ["didn't work", "still", "no", "not working", "failed", "nothing", "same", "still not", "still no"]

        solution_worked = None
        if any(kw in message_lower for kw in success_keywords):
            solution_worked = True
        elif any(kw in message_lower for kw in failure_keywords):
            solution_worked = False

        return {
            'tried_solution': solution_name is not None,
            'solution_worked': solution_worked,
            'solution_name': solution_name
        }

    def get_context_for_llm(self) -> str:
        """Generate context string for LLM prompt"""
        if not self.is_active():
            return ""

        context_parts = []

        if self.attempted_solutions:
            solutions_str = ', '.join(self.attempted_solutions)
            context_parts.append(
                f"User has already tried these solutions: {solutions_str}. "
                f"DO NOT suggest these again."
            )

        if self.diagnostic_answers:
            answers_list = [f"{q}: {a}" for q, a in self.diagnostic_answers.items()]
            answers_str = " | ".join(answers_list)
            context_parts.append(f"Diagnostic information gathered: {answers_str}")

        if self.questions_asked > 0:
            context_parts.append(f"Questions asked so far: {self.questions_asked}")

        context_parts.append(f"Current confidence level: {self.confidence_level}")

        if self.flow_id:
            context_parts.append(f"Current diagnostic flow: {self.flow_id}")

        return "\n".join(context_parts)


class SessionManager:
    """Manage multiple user sessions"""

    def __init__(self):
        self.sessions: Dict[str, DiagnosticSession] = {}

    def get_session(self, user_id: str) -> DiagnosticSession:
        """Get or create session for user"""
        if user_id not in self.sessions:
            self.sessions[user_id] = DiagnosticSession(user_id)

        session = self.sessions[user_id]

        # Reset if inactive
        if not session.is_active():
            self.sessions[user_id] = DiagnosticSession(user_id)
            return self.sessions[user_id]

        return session

    def clear_session(self, user_id: str):
        """Clear user's session"""
        if user_id in self.sessions:
            del self.sessions[user_id]

    def cleanup_inactive(self, timeout_minutes: int = 30):
        """Remove inactive sessions"""
        to_remove = [
            uid for uid, session in self.sessions.items()
            if not session.is_active(timeout_minutes)
        ]
        for uid in to_remove:
            del self.sessions[uid]
