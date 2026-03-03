import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

class EmbeddingEngine:
    def __init__(self, persist_directory="./chroma_db"):
        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_store = Chroma(
            collection_name="news_articles",
            embedding_function=self.embeddings,
            persist_directory=self.persist_directory
        )

    def clear_articles(self):
        existing_docs = self.vector_store.get()
        if existing_docs and existing_docs.get("ids"):
            self.vector_store.delete(ids=existing_docs["ids"])

    def add_articles(self, documents, clear_first=True):
        if clear_first:
            self.clear_articles()
        if documents:
            self.vector_store.add_documents(documents=documents)

    def search_articles(self, query, k=5):
        return self.vector_store.similarity_search(query, k=k)
