"""Text cleaning utilities for news articles."""
import re


def clean_text(text: str) -> str:
    """Remove HTML tags, extra whitespace, and special characters."""
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def clean_article(article: dict) -> dict:
    """Clean title and content fields of an article."""
    article["title"] = clean_text(article.get("title", ""))
    article["content"] = clean_text(article.get("content", ""))
    return article
