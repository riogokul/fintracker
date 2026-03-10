"""FastAPI application entry point."""
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from .routes import news, summaries

app = FastAPI(title="Financial News Summarizer API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news.router, prefix="/api/v1")
app.include_router(summaries.router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.websocket("/ws/news")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time news updates."""
    await websocket.accept()
    # TODO: Implement real-time push logic
    await websocket.close()
