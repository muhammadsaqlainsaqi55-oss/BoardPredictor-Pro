import re
from collections import Counter

def analyze_trends(text):
    """Analyzes C Language keyword frequency from extracted text."""
    keywords = [
        'pointer', 'array', 'structure', 'union', 'function', 
        'recursion', 'file handling', 'printf', 'scanf', 'loop',
        'while', 'for', 'switch', 'if else', 'data types', 
        'variable', 'header file', 'operator', 'constant'
    ]
    text = text.lower()
    found_keywords = []
    for word in keywords:
        matches = re.findall(rf'\b{word}\b', text)
        for _ in range(len(matches)):
            found_keywords.append(word.title())
    counts = Counter(found_keywords)
    return dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

if __name__ == "__main__":
    print("C Language Pattern Analyzer Ready.")
