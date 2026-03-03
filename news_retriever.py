import os
import requests
from langchain_core.documents import Document

class NewsRetriever:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2/everything"

    def get_articles(self, topic, page_size=10):
        if not self.api_key:
            raise ValueError("NewsAPI key is required.")
        
        params = {
            "q": topic,
            "apiKey": self.api_key,
            "language": "en",
            "pageSize": page_size,
            "sortBy": "relevancy"
        }
        
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        articles = data.get("articles", [])
        documents = []
        
        for article in articles:
            content = article.get("content") or article.get("description")
            title = article.get("title")
            
            if content and title and "[Removed]" not in title:
                full_text = f"Title: {title}\n\n{content}"
                metadata = {
                    "source": article.get("url", ""),
                    "title": title,
                    "author": article.get("author", "") or "Unknown",
                    "publishedAt": article.get("publishedAt", "")
                }
                
                doc = Document(
                    page_content=full_text,
                    metadata=metadata
                )
                documents.append(doc)
                
        return documents
