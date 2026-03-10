"""News-related API routes."""
from fastapi import APIRouter, Query

router = APIRouter(tags=["news"])


@router.get("/news/search")
async def search_news(q: str = Query(..., min_length=3)):
    """Search articles by keyword query."""
    # TODO: Implement search via RAG retriever
    return {"query": q, "results": []}


@router.get("/news/realtime")
async def get_realtime_news():
    """Get the latest ingested news articles."""
    # TODO: Fetch from DB or Redis stream
    return {"articles": []}
