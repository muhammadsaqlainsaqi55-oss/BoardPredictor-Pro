from collections import Counter
from typing import Dict, List
import re


# Core C language keywords we want to track across board papers
C_KEYWORDS: List[str] = [
    "pointers",
    "arrays",
    "loops",
    "struct",
    "file handling",
    "functions",
    "header files",
    "recursion",
]


def _tokenize(text: str) -> List[str]:
    """
    Normalize and tokenize text into lowercase word tokens.

    We keep underscores and alphanumeric characters (useful for code-like
    tokens), and treat all contiguous non-matching characters as separators.
    """
    lower = text.lower()
    normalized = re.sub(r"[^a-z0-9_]+", " ", lower)
    return normalized.split()


def count_keywords(text: str, keywords: List[str]) -> Dict[str, int]:
    """
    Count occurrences of specified keywords in text.

    - Case-insensitive.
    - Matches whole tokens (e.g., 'struct' will not match 'destructor').
    """
    tokens = _tokenize(text)
    token_counts = Counter(tokens)

    result: Dict[str, int] = {}
    for kw in keywords:
        key = kw.strip().lower()
        if not key:
            continue
        # For multi-word phrases (e.g., "file handling"), fall back to a simple
        # case-insensitive substring count over the original text.
        if " " in key:
            pattern = re.escape(key)
            count = len(re.findall(pattern, text.lower()))
            result[kw] = count
        else:
            result[kw] = token_counts.get(key, 0)

    return result


