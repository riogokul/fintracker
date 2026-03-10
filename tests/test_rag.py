"""Tests for RAG engine components."""
import pytest
from src.rag.embeddings import EmbeddingModel


def test_embedding_dimensions():
    model = EmbeddingModel()
    embedding = model.embed_query("Tesla stock rises 5% on earnings beat")
    assert len(embedding) == 384  # MiniLM-L6-v2 output dimension


def test_embed_batch():
    model = EmbeddingModel()
    texts = ["Apple earnings report", "Fed interest rate decision"]
    embeddings = model.embed(texts)
    assert len(embeddings) == 2
