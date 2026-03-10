"""Deduplication logic to avoid storing duplicate articles."""
from typing import List, Dict


class Deduplicator:
    def __init__(self):
        self._seen_urls: set = set()

    def is_duplicate(self, article: Dict) -> bool:
        """Check if article URL has already been seen."""
        url = article.get("url", "")
        if url in self._seen_urls:
            return True
        self._seen_urls.add(url)
        return False

    def deduplicate(self, articles: List[Dict]) -> List[Dict]:
        """Filter out duplicate articles from a list."""
        return [a for a in articles if not self.is_duplicate(a)]
