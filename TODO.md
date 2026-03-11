# fintracker — TODO

## In Progress

_Nothing started yet._

---

## Pending

### Phase 1 — Setup & Infrastructure

- [ - ] Add all missing dependencies to `pyproject.toml`
      (langchain, langchain-community, chromadb, sentence-transformers, redis,
      praw, aiohttp, feedparser, beautifulsoup4, pydantic-settings, yfinance,
      textblob, sqlalchemy, alembic, psycopg2-binary, streamlit, plotly, pytest, etc.)
- [ ] Create `.env.example` with all required environment variables
      (DATABASE_URL, REDIS_URL, API keys, OLLAMA settings, RAG settings)
- [ - ] Create `docker-compose.yml` for PostgreSQL, Redis, ChromaDB
- [ - ] Create `deployment/docker/Dockerfile.api`
- [ - ] Create `deployment/docker/Dockerfile.frontend`
- [ ] Create `scripts/init_db.py` to initialise PostgreSQL schema (articles + summaries tables)
- [ ] Set up Alembic for database migrations
- [ - ] Create data directories: `data/raw/`, `data/processed/`, `data/embeddings/`
- [ ] Update `main.py` — currently just prints hello; wire it as a proper app entrypoint
      (start API + scheduler or print usage)

### Phase 2 — Data Ingestion

- [ ] Implement `CNBCScraper.scrape()` using BeautifulSoup
      `src/data_ingestion/scrapers/cnbc_scraper.py`
- [ ] Implement `RedditScraper.fetch_posts()` using PRAW
      `src/data_ingestion/scrapers/reddit_scraper.py`
- [ ] Integrate Finnhub / NewsAPI / Alpha Vantage API clients into `NewsFetcher`
      `src/data_ingestion/news_fetcher.py`
- [ ] Create `scripts/fetch_historical_data.py` to bootstrap the database with initial articles

### Phase 3 — Preprocessing

- [ ] Implement `SentimentAnalyzer.analyze()` using TextBlob or FinBERT
      `src/preprocessing/sentiment_analyzer.py`
- [ ] Add entity extraction (companies, tickers, people) to the preprocessing pipeline
- [ ] Persist cleaned + annotated articles to PostgreSQL via SQLAlchemy

### Phase 4 — RAG Pipeline

- [ ] Wire `EmbeddingModel` + `VectorStore` + `Retriever` + `Summarizer` into a single `RAGEngine` class
- [ ] Add document ingestion script: clean → embed → store in ChromaDB
- [ ] Implement sector-specific and ticker-specific summarization in `Summarizer`
      `src/rag/summarizer.py`

### Phase 5 — API Routes

- [ ] Wire `search_news` to `Retriever.retrieve()` and return `ArticleSchema` list
      `src/api/routes/news.py`
- [ ] Wire `get_realtime_news` to fetch latest articles from DB / Redis stream
      `src/api/routes/news.py`
- [ ] Wire `get_daily_summary` to `Summarizer.daily_summary()`
      `src/api/routes/summaries.py`
- [ ] Wire `get_ticker_summary` to filter + summarize by symbol
      `src/api/routes/summaries.py`
- [ ] Wire `custom_summary` to `Summarizer.summarize()` with retrieved context
      `src/api/routes/summaries.py`
- [ ] Wire `get_sentiment` to `SentimentAnalyzer` aggregated over recent articles
      `src/api/routes/summaries.py`
- [ ] Implement WebSocket real-time push logic (broadcast new articles to connected clients)
      `src/api/main.py` — `websocket_endpoint()`
- [ ] Add Redis caching layer for frequent API queries (daily summary, sentiment)
- [ ] Add JWT authentication / API key security to protected endpoints

### Phase 6 — Frontend

- [ ] Implement `render_news_feed()` — fetch `/api/v1/news/realtime` and display articles
      `src/frontend/components/news_feed.py`
- [ ] Implement `render_summary_viewer()` — fetch `/api/v1/summary/daily` and display
      `src/frontend/components/summary_viewer.py`
- [ ] Add Plotly sentiment chart to Top Movers panel
      `src/frontend/app.py`
- [ ] Add search bar wired to `/api/v1/news/search`
      `src/frontend/app.py`
- [ ] Fix import paths in `src/frontend/app.py` (currently uses bare `components.*` imports)

### Phase 7 — Testing

- [ ] Write unit tests for `NewsFetcher`, `Deduplicator`, `TextCleaner`
      `tests/test_ingestion.py`
- [ ] Write unit tests for `EmbeddingModel`, `VectorStore`, `Retriever`, `Summarizer`
      `tests/test_rag.py`
- [ ] Write integration tests for all API endpoints
      `tests/test_api.py`
- [ ] Add pytest config and coverage reporting to `pyproject.toml`
- [ ] Write load tests using Locust (`locustfile.py`)

### Phase 8 — Deployment & Monitoring

- [ ] Add Prometheus metrics middleware to FastAPI app
      `src/api/main.py`
- [ ] Configure structured logging (loguru / python-json-logger)
- [ ] Create `deployment/kubernetes/deployment.yaml` and `service.yaml`
- [ ] Create Jupyter notebooks: `notebooks/data_exploration.ipynb`, `notebooks/rag_testing.ipynb`

---

## Completed

_Nothing completed yet._
