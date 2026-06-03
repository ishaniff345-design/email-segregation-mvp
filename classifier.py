"""
Classifier for email categorization.
Uses keyword counting and pattern matching to classify emails.
"""

from patterns import (
    TONNAGE_KEYWORDS,
    CARGO_VC_KEYWORDS,
    CARGO_TC_KEYWORDS,
    PATTERNS,
    get_keyword_count,
)


class EmailClassifier:
    """Classifies shipping emails into categories."""

    def __init__(self):
        """Initialize classifier with patterns."""
        self.patterns = PATTERNS

    def classify(self, email_text: str) -> tuple[str, float]:
        """
        Classify email and return category with confidence score.
        
        Args:
            email_text: Raw email text
            
        Returns:
            Tuple of (category, confidence) where:
            - category: 'tonnage', 'cargo_vc', 'cargo_tc', or 'unknown'
            - confidence: float between 0.0 and 1.0
        """
        # Count keyword matches for each category
        tonnage_count = get_keyword_count(email_text, TONNAGE_KEYWORDS)
        cargo_vc_count = get_keyword_count(email_text, CARGO_VC_KEYWORDS)
        cargo_tc_count = get_keyword_count(email_text, CARGO_TC_KEYWORDS)

        # Find category with highest keyword count
        max_count = max(tonnage_count, cargo_vc_count, cargo_tc_count)

        if max_count == 0:
            return 'unknown', 0.0

        # Determine category
        if tonnage_count == max_count:
            category = 'tonnage'
            keyword_score = tonnage_count / len(TONNAGE_KEYWORDS)
        elif cargo_tc_count == max_count:
            # Cargo TC takes priority over VC if counts are equal
            category = 'cargo_tc'
            keyword_score = cargo_tc_count / len(CARGO_TC_KEYWORDS)
        else:
            category = 'cargo_vc'
            keyword_score = cargo_vc_count / len(CARGO_VC_KEYWORDS)

        # Cap score at 1.0 and add small bonus for strong signals
        confidence = min(keyword_score, 1.0)
        if max_count >= 3:
            confidence = min(confidence + 0.1, 1.0)

        return category, confidence

    def get_category_scores(self, email_text: str) -> dict[str, float]:
        """
        Get scores for all categories.
        
        Returns:
            Dictionary with category: score pairs
        """
        tonnage_count = get_keyword_count(email_text, TONNAGE_KEYWORDS)
        cargo_vc_count = get_keyword_count(email_text, CARGO_VC_KEYWORDS)
        cargo_tc_count = get_keyword_count(email_text, CARGO_TC_KEYWORDS)

        total = tonnage_count + cargo_vc_count + cargo_tc_count
        if total == 0:
            return {'tonnage': 0.0, 'cargo_vc': 0.0, 'cargo_tc': 0.0}

        return {
            'tonnage': round(tonnage_count / total, 2),
            'cargo_vc': round(cargo_vc_count / total, 2),
            'cargo_tc': round(cargo_tc_count / total, 2),
        }
