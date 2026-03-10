"""Pydantic schemas for request/response models."""
from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime


class ArticleSchema(BaseModel):
    title: str
    content: Optional[str] = None
    url: str
    source: str
    published_at: Optional[datetime] = None
    sentiment_score: Optional[float] = None


class SummarySchema(BaseModel):
    date: Optional[str] = None
    summary_type: str
    content: str
    article_ids: list[int] = []


class CustomQueryRequest(BaseModel):
    query: str
    max_results: int = 5

    @field_validator("query")
    @classmethod
    def validate_query(cls, v: str) -> str:
        if len(v) < 3:
            raise ValueError("Query must be at least 3 characters")
        return v
