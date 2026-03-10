"""LLM-based summarization using RAG."""
from typing import List, Dict
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


SUMMARY_TEMPLATE = """You are a financial news analyst. Based on the following news articles, provide a concise summary focusing on key market insights and trading implications.

Context Articles:
{context}

Question: {question}

Provide a clear, structured summary with:
1. Key Market Movements
2. Major News Events
3. Trading Implications
4. Risk Factors

Summary:"""


class Summarizer:
    def __init__(self, ollama_model: str = "mistral", ollama_host: str = "http://localhost:11434"):
        self.llm = Ollama(model=ollama_model, base_url=ollama_host, temperature=0.3)
        self.prompt = PromptTemplate(
            template=SUMMARY_TEMPLATE,
            input_variables=["context", "question"],
        )

    def summarize(self, query: str, context_docs: List[Dict]) -> str:
        """Generate a summary given a query and retrieved context documents."""
        context = "\n\n".join(
            doc.get("content", "") for doc in context_docs
        )
        formatted_prompt = self.prompt.format(context=context, question=query)
        return self.llm(formatted_prompt)

    def daily_summary(self, date: str = "today") -> str:
        """Generate a daily market summary."""
        query = f"What are the key market developments and trading insights for {date}?"
        return self.summarize(query, [])
