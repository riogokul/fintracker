"""Sentiment analysis for financial news articles."""
from typing import Dict


class SentimentAnalyzer:
    def __init__(self):
        # TODO: Initialize NLP model (e.g., TextBlob, FinBERT)
        pass

    def analyze(self, text: str) -> float:
        """Return sentiment score between -1.0 (negative) and 1.0 (positive)."""
        # TODO: Implement sentiment scoring
        raise NotImplementedError

    def annotate_article(self, article: Dict) -> Dict:
        """Add sentiment_score field to article dict."""
        text = f"{article.get('title', '')} {article.get('content', '')}"
        article["sentiment_score"] = self.analyze(text)
        return article
