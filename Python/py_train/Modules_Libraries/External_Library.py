# ⚠️ First, install the package:
# pip install textblob

# 🧠 Initialize textblob once if needed:
# python -m textblob.download_corpora

from textblob import TextBlob

def get_sentiment(text: str) -> str:
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"
