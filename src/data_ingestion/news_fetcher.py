"""RSS/API fetching for financial news."""
import asyncio
import aiohttp
import feedparser
from typing import List, Dict
from datetime import datetime


RSS_FEEDS = [
    "http://feeds.reuters.com/reuters/businessNews",
    "https://finance.yahoo.com/news/rssindex",
    "http://feeds.marketwatch.com/marketwatch/topstories/",
]


class NewsFetcher:
    def __init__(self):
        self.rss_feeds = RSS_FEEDS

    async def fetch_rss_async(self, url: str) -> List[Dict]:
        """Fetch RSS feed asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.text()
                feed = feedparser.parse(content)
                return self._parse_feed(feed)

    def _parse_feed(self, feed) -> List[Dict]:
        """Parse RSS feed into standardized format."""
        articles = []
        for entry in feed.entries:
            article = {
                "title": entry.get("title", ""),
                "content": entry.get("summary", ""),
                "url": entry.get("link", ""),
                "published_at": entry.get("published", ""),
                "source": feed.feed.get("title", "Unknown"),
                "author": entry.get("author", ""),
            }
            articles.append(article)
        return articles

    async def fetch_all(self) -> List[Dict]:
        """Fetch from all sources concurrently."""
        tasks = [self.fetch_rss_async(url) for url in self.rss_feeds]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        all_articles = []
        for result in results:
            if isinstance(result, list):
                all_articles.extend(result)
        return all_articles
