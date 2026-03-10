"""Semantic search / retrieval over the vector store."""
from typing import List, Dict
from .embeddings import EmbeddingModel
from .vector_store import VectorStore


class Retriever:
    def __init__(self, embedding_model: EmbeddingModel, vector_store: VectorStore):
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def retrieve(self, query: str, k: int = 5) -> List[Dict]:
        """Retrieve top-k relevant documents for a query."""
        query_embedding = self.embedding_model.embed_query(query)
        results = self.vector_store.query(query_embedding, n_results=k)
        return results
