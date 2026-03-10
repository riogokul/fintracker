"""Tests for FastAPI endpoints."""
import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_daily_summary_endpoint():
    response = client.get("/api/v1/summary/daily")
    assert response.status_code == 200


def test_news_search_requires_query():
    response = client.get("/api/v1/news/search")
    assert response.status_code == 422  # Missing required query param
