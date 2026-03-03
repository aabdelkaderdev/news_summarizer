import streamlit as st
import os
from user_manager import UserManager
from news_retriever import NewsRetriever
from embedding_engine import EmbeddingEngine
from summarizer import NewsSummarizer

st.set_page_config(page_title="News Summarizer", layout="wide")

st.title("News Summarizer Application")

if "user_manager" not in st.session_state:
    st.session_state.user_manager = UserManager()

news_api_key = st.sidebar.text_input("NewsAPI Key", value=os.environ.get("NEWS_API_KEY", ""), type="password")
groq_api_key = st.sidebar.text_input("Groq API Key", value=os.environ.get("GROQ_API_KEY", ""), type="password")

if not news_api_key or not groq_api_key:
    st.warning("Please provide both NewsAPI and Groq API keys in the sidebar to continue.")
    st.stop()

@st.cache_resource
def get_embedding_engine():
    return EmbeddingEngine()

retriever = NewsRetriever(api_key=news_api_key)
embedder = get_embedding_engine()
summarizer = NewsSummarizer(api_key=groq_api_key)

tab1, tab2, tab3 = st.tabs(["Search News", "Saved Topics", "Search History"])

with tab1:
    st.header("Search and Summarize News")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        topic_input = st.text_input("Enter a topic to search for news:", key="search_input")
    with col2:
        summary_style = st.selectbox("Summary Style:", ["Brief", "Detailed"])
        
    if st.button("Search"):
        if topic_input:
            st.session_state.user_manager.add_search_history(topic_input)
            
            with st.spinner("Fetching news..."):
                try:
                    articles = retriever.get_articles(topic_input, page_size=5)
                    if not articles:
                        st.info("No articles found.")
                    else:
                        embedder.add_articles(articles)
                        
                        relevant_docs = embedder.search_articles(topic_input, k=3)
                        
                        for i, doc in enumerate(relevant_docs):
                            st.subheader(f"{i+1}. {doc.metadata.get('title', 'Unknown Title')}")
                            st.write(f"Source: {doc.metadata.get('source', 'Unknown')} | Author: {doc.metadata.get('author', 'Unknown')}")
                            
                            with st.spinner("Summarizing..."):
                                if summary_style == "Brief":
                                    summary = summarizer.summarize_brief(doc.page_content)
                                else:
                                    summary = summarizer.summarize_detailed(doc.page_content)
                                    
                                st.write("**Summary:**")
                                st.write(summary)
                                st.markdown("---")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a topic.")

with tab2:
    st.header("Manage Saved Topics")
    
    new_topic = st.text_input("Add a new topic of interest:")
    if st.button("Save Topic"):
        if new_topic:
            st.session_state.user_manager.add_topic(new_topic)
            st.rerun()
            
    saved_topics = st.session_state.user_manager.get_saved_topics()
    
    if saved_topics:
        for topic in saved_topics:
            col_a, col_b = st.columns([4, 1])
            with col_a:
                st.write(f"- {topic}")
            with col_b:
                if st.button("Remove", key=f"remove_{topic}"):
                    st.session_state.user_manager.remove_topic(topic)
                    st.rerun()
    else:
        st.info("No saved topics.")

with tab3:
    st.header("Search History")
    
    history = st.session_state.user_manager.get_search_history()
    
    if history:
        if st.button("Clear History"):
            st.session_state.user_manager.clear_search_history()
            st.rerun()
            
        for entry in reversed(history):
            st.write(f"**Query:** {entry['query']} | **Time:** {entry['timestamp']}")
    else:
        st.info("History is empty.")