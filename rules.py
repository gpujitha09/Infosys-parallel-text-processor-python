POSITIVE = {"good", "great", "excellent", "awesome", "nice"}
NEGATIVE = {"bad", "poor", "worst", "terrible", "awful"}

def score_text(text):
    words = text.lower().split()
    pos = sum(1 for w in words if w in POSITIVE)
    neg = sum(1 for w in words if w in NEGATIVE)
    return pos - neg
