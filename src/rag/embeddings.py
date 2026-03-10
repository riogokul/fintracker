"""Embedding generation using sentence-transformers."""
from typing import List
from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts."""
        return self.model.encode(texts).tolist()

    def embed_query(self, text: str) -> List[float]:
        """Generate embedding for a single query string."""
        return self.model.encode([text])[0].tolist()
