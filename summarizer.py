import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

class NewsSummarizer:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("Groq API key is required.")
        
        self.llm = ChatGroq(
            api_key=self.api_key,
            model_name="llama-3.1-8b-instant",
            temperature=0.3
        )

        self.brief_prompt = PromptTemplate(
            template="Provide a brief summary (1-2 sentences) of the following news article. Do not use any emojis.\n\nArticle: {article}\n\nBrief Summary:",
            input_variables=["article"]
        )

        self.detailed_prompt = PromptTemplate(
            template="Provide a detailed paragraph summary of the following news article. Do not use any emojis.\n\nArticle: {article}\n\nDetailed Summary:",
            input_variables=["article"]
        )

        self.brief_chain = self.brief_prompt | self.llm
        self.detailed_chain = self.detailed_prompt | self.llm

    def summarize_brief(self, article_text):
        response = self.brief_chain.invoke({"article": article_text})
        return response.content

    def summarize_detailed(self, article_text):
        response = self.detailed_chain.invoke({"article": article_text})
        return response.content