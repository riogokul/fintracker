"""CNBC Markets web scraper."""
from typing import List, Dict


class CNBCScraper:
    def __init__(self):
        self.base_url = "https://www.cnbc.com/markets/"

    def scrape(self) -> List[Dict]:
        """Scrape latest market headlines from CNBC."""
        # TODO: Implement scraping logic
        raise NotImplementedError
