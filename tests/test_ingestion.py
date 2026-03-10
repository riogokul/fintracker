"""Tests for data ingestion pipeline."""
import pytest
from src.data_ingestion.news_fetcher import NewsFetcher


@pytest.mark.asyncio
async def test_fetch_all_returns_list():
    fetcher = NewsFetcher()
    articles = await fetcher.fetch_all()
    assert isinstance(articles, list)


def test_parse_feed_fields():
    fetcher = NewsFetcher()
    # TODO: Add mock feed and assert required fields
    pass
