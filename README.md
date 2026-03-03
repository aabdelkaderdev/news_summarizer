# News Summarizer Application

A Streamlit-based web application that retrieves news articles on specific topics using NewsAPI, generates vector embeddings for semantic search using Chroma and HuggingFace, and provides concise or detailed summaries using LangChain and Groq's Llama-3.1-8B-Instruct model. The app also tracks your search history and saved topics locally.

## Features
- **Article Retrieval**: Fetches top news articles on user-specified topics via NewsAPI.
- **Semantic Search Base**: Uses `all-MiniLM-L6-v2` embeddings stored in a Chroma vector database to find the most relevant articles for summarization.
- **AI Summarization**: Powered by `ChatGroq` (`meta-llama/llama3-8b-8192`) to provide quick Brief (1-2 sentences) or Detailed (paragraph) summaries.
- **Preference Tracking**: Saves user topics and tracks search history in a local JSON file.

## Demo
Try the application live on Streamlit Community Cloud:  
**🔗 [Streamlit Demo](https://newssummarizer-e3fjlb2khxehelgbhmltve.streamlit.app/)**

---

## Deployment Instructions

### Option 1: Local Deployment

#### Prerequisites
- Python 3.8+
- [NewsAPI Key](https://newsapi.org/register)
- [Groq API Key](https://console.groq.com/keys)

#### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aabdelkaderdev/news_summarizer.git
   cd news_summarizer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables:**
   The application requires your API keys to be set as environment variables.
   
   *On Linux/macOS:*
   ```bash
   export NEWS_API_KEY="your_news_api_key_here"
   export GROQ_API_KEY="your_groq_api_key_here"
   ```
   
   *On Windows (Command Prompt):*
   ```cmd
   set NEWS_API_KEY=your_news_api_key_here
   set GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application:**
   ```bash
   streamlit run main.py
   ```
   The app will open automatically in your browser at `http://localhost:8501`.

---

### Option 2: Streamlit Community Cloud Deployment

1. **Host on GitHub:** Ensure this repository is pushed to your GitHub account.
2. **Deploy on Streamlit:**
   - Go to [Streamlit Community Cloud](https://share.streamlit.io/).
   - Click **New app** and select your `news_summarizer` repository.
   - Set the **Main file path** to `main.py`.
3. **Configure Secrets:**
   - Before clicking "Deploy", click on **Advanced settings...**.
   - Under the **Secrets** section, add your API keys:
     ```toml
     NEWS_API_KEY = "your-news-api-key-here"
     GROQ_API_KEY = "your-groq-api-key-here"
     ```
   - Click **Save**.
4. **Launch:** Click **Deploy!** Your app will build and launch automatically.
