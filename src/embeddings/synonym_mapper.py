"""
Synonym Mapper - Handles terminology variance for better retrieval
"""

import json
from pathlib import Path
from typing import Dict, List, Set
import logging

logger = logging.getLogger(__name__)


class SynonymMapper:
    """Maps user terminology to canonical terms and expands queries"""

    def __init__(self, glossary_path: str):
        """
        Args:
            glossary_path: Path to glossary.json
        """
        self.glossary_path = Path(glossary_path)
        self.glossary = self._load_glossary()
        self.term_to_canonical = self._build_lookup_map()

    def _load_glossary(self) -> Dict:
        """Load glossary from JSON file"""
        if not self.glossary_path.exists():
            logger.warning(f"Glossary not found: {self.glossary_path}")
            return {}

        with open(self.glossary_path, 'r') as f:
            glossary = json.load(f)

        # Remove comment key
        glossary.pop('_comment', None)

        logger.info(f"Loaded {len(glossary)} synonym groups from glossary")
        return glossary

    def _build_lookup_map(self) -> Dict[str, str]:
        """Build fast lookup map: synonym -> canonical term"""
        lookup = {}

        for group_name, group_data in self.glossary.items():
            canonical = group_data['canonical']
            synonyms = group_data['synonyms']

            # Map all synonyms to canonical term
            for syn in synonyms:
                lookup[syn.lower()] = canonical

        logger.info(f"Built lookup map with {len(lookup)} terms")
        return lookup

    def expand_query(self, query: str) -> str:
        """
        Expand query with synonyms for better matching

        Example: "boss won't start" -> "boss won't start IPTVBoss crash freeze"

        Args:
            query: User query

        Returns:
            Expanded query string
        """
        query_lower = query.lower()
        added_terms = set()

        # Find matching terms in query
        for term, canonical in self.term_to_canonical.items():
            if term in query_lower:
                # Add canonical term if not already in query
                if canonical.lower() not in query_lower:
                    added_terms.add(canonical)

                # Add a few key synonyms
                group = self._find_group_by_canonical(canonical)
                if group:
                    synonyms = group['synonyms'][:2]  # Add top 2 synonyms
                    for syn in synonyms:
                        if syn.lower() not in query_lower:
                            added_terms.add(syn)

        # Build expanded query
        if added_terms:
            expanded = query + " " + " ".join(added_terms)
            logger.debug(f"Expanded query: '{query}' -> '{expanded}'")
            return expanded

        return query

    def _find_group_by_canonical(self, canonical: str) -> Dict:
        """Find synonym group by canonical term"""
        for group_data in self.glossary.values():
            if group_data['canonical'] == canonical:
                return group_data
        return None

    def add_synonym_metadata(self, chunk: Dict) -> Dict:
        """
        Add synonym tags to chunk metadata for better retrieval

        Args:
            chunk: Chunk dict with 'text' key

        Returns:
            Chunk with added 'synonyms' metadata
        """
        text_lower = chunk['text'].lower()
        found_terms = set()

        # Find all matching terms in chunk text
        for term, canonical in self.term_to_canonical.items():
            if term in text_lower:
                found_terms.add(canonical)

        # Add to chunk metadata
        chunk['synonyms'] = list(found_terms)

        return chunk
