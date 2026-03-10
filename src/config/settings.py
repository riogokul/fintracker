from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql://admin:password@localhost:5432/financial_news"
    redis_url: str = "redis://localhost:6379/0"

    # API Keys
    newsapi_key: str = ""
    alpha_vantage_key: str = ""
    finnhub_key: str = ""
    reddit_client_id: str = ""
    reddit_client_secret: str = ""

    # LLM Settings
    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "mistral"

    # Application
    app_name: str = "Financial News Summarizer"
    app_version: str = "1.0.0"
    debug: bool = False
    log_level: str = "INFO"

    # Streaming
    max_stream_length: int = 10000
    consumer_group: str = "news_processors"

    # RAG Settings
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    vector_store_path: str = "./data/chroma"
    top_k_results: int = 5
    chunk_size: int = 500
    chunk_overlap: int = 50

    # Caching
    cache_ttl: int = 3600

    class Config:
        env_file = ".env"


settings = Settings()
