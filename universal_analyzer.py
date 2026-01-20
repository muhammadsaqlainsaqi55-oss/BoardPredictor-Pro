import re
from collections import Counter

def analyze_trends(text):
    # Extracts words longer than 4 letters to find meaningful topics
    words = re.findall(r'\b[A-Za-z]{5,}\b', text.lower()) 
    stop_words = {'which', 'there', 'their', 'would', 'should', 'these', 'those'}
    filtered = [w for w in words if w not in stop_words]
    return dict(Counter(filtered).most_common(15))
