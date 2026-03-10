"""Summary-related API routes."""
from fastapi import APIRouter
from ..models.schemas import CustomQueryRequest

router = APIRouter(tags=["summaries"])


@router.get("/summary/daily")
async def get_daily_summary():
    """Return today's daily market summary."""
    # TODO: Call summarizer.daily_summary()
    return {"summary": ""}


@router.get("/summary/ticker/{symbol}")
async def get_ticker_summary(symbol: str):
    """Return a summary for a specific stock ticker."""
    # TODO: Filter news by symbol and summarize
    return {"symbol": symbol, "summary": ""}


@router.post("/summary/custom")
async def custom_summary(request: CustomQueryRequest):
    """Generate a summary for a custom query."""
    # TODO: Call summarizer.summarize(request.query, ...)
    return {"query": request.query, "summary": ""}


@router.get("/sentiment/{symbol}")
async def get_sentiment(symbol: str):
    """Return sentiment score for a stock symbol."""
    # TODO: Aggregate sentiment from recent articles
    return {"symbol": symbol, "sentiment": None}
