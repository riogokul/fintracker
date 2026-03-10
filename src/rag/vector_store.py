"""ChromaDB vector store operations."""
from typing import List, Dict
import chromadb


class VectorStore:
    def __init__(self, persist_directory: str = "./data/chroma"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection("financial_news")

    def add_documents(self, texts: List[str], embeddings: List[List[float]], metadatas: List[Dict], ids: List[str]):
        """Add documents with pre-computed embeddings to the store."""
        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )

    def query(self, query_embedding: List[float], n_results: int = 5) -> Dict:
        """Query the vector store for similar documents."""
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
        )

    def count(self) -> int:
        """Return number of documents in the collection."""
        return self.collection.count()
