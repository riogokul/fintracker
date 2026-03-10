"""Reddit scraper for financial subreddits."""
from typing import List, Dict


SUBREDDITS = ["wallstreetbets", "investing", "stocks"]


class RedditScraper:
    def __init__(self, client_id: str, client_secret: str, user_agent: str = "fintracker"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent

    def fetch_posts(self, subreddit: str, limit: int = 25) -> List[Dict]:
        """Fetch top posts from a subreddit."""
        # TODO: Implement using PRAW
        raise NotImplementedError

    def fetch_all(self) -> List[Dict]:
        """Fetch posts from all configured subreddits."""
        all_posts = []
        for sub in SUBREDDITS:
            all_posts.extend(self.fetch_posts(sub))
        return all_posts
