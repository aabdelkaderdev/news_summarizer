[Skip to main content](https://docs.langchain.com/oss/python/integrations/document_loaders#content-area)

[Docs by LangChain home page![light logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-dark-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=5babf1a1962208fd7eed942fa2432ecb)![dark logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-light-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=0bcd2a1f2599ed228bcedf0f535b45b1)](https://docs.langchain.com/)

![https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png](https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png)Open source

Search...

Ctrl K

Search...

Navigation

Integrations by component

Document loader integrations

[Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) [LangChain](https://docs.langchain.com/oss/python/langchain/overview) [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) [Integrations](https://docs.langchain.com/oss/python/integrations/providers/overview) [Learn](https://docs.langchain.com/oss/python/learn) [Reference](https://docs.langchain.com/oss/python/reference/overview) [Contribute](https://docs.langchain.com/oss/python/contributing/overview)

Python

- [LangChain integrations](https://docs.langchain.com/oss/python/integrations/providers/overview)

- [All providers](https://docs.langchain.com/oss/python/integrations/providers/all_providers)

##### Popular Providers

- [OpenAI](https://docs.langchain.com/oss/python/integrations/providers/openai)
- [Anthropic](https://docs.langchain.com/oss/python/integrations/providers/anthropic)
- [Google](https://docs.langchain.com/oss/python/integrations/providers/google)
- [AWS](https://docs.langchain.com/oss/python/integrations/providers/aws)
- [Hugging Face](https://docs.langchain.com/oss/python/integrations/providers/huggingface)
- [Microsoft](https://docs.langchain.com/oss/python/integrations/providers/microsoft)
- [Ollama](https://docs.langchain.com/oss/python/integrations/providers/ollama)
- [Groq](https://docs.langchain.com/oss/python/integrations/providers/groq)
- [NVIDIA](https://docs.langchain.com/oss/python/integrations/providers/nvidia)

##### Integrations by component

- [Chat models](https://docs.langchain.com/oss/python/integrations/chat)
- [Tools and toolkits](https://docs.langchain.com/oss/python/integrations/tools)
- [Middleware](https://docs.langchain.com/oss/python/integrations/middleware)
- [Retrievers](https://docs.langchain.com/oss/python/integrations/retrievers)
- [Text splitters](https://docs.langchain.com/oss/python/integrations/splitters)
- [Embedding models](https://docs.langchain.com/oss/python/integrations/text_embedding)
- [Vector stores](https://docs.langchain.com/oss/python/integrations/vectorstores)
- [Document loaders](https://docs.langchain.com/oss/python/integrations/document_loaders)
- [Key-value stores](https://docs.langchain.com/oss/python/integrations/stores)

On this page

- [Interface](https://docs.langchain.com/oss/python/integrations/document_loaders#interface)
- [By category](https://docs.langchain.com/oss/python/integrations/document_loaders#by-category)
- [Webpages](https://docs.langchain.com/oss/python/integrations/document_loaders#webpages)
- [PDFs](https://docs.langchain.com/oss/python/integrations/document_loaders#pdfs)
- [Cloud providers](https://docs.langchain.com/oss/python/integrations/document_loaders#cloud-providers)
- [Social platforms](https://docs.langchain.com/oss/python/integrations/document_loaders#social-platforms)
- [Messaging services](https://docs.langchain.com/oss/python/integrations/document_loaders#messaging-services)
- [Productivity tools](https://docs.langchain.com/oss/python/integrations/document_loaders#productivity-tools)
- [Common file types](https://docs.langchain.com/oss/python/integrations/document_loaders#common-file-types)
- [All document loaders](https://docs.langchain.com/oss/python/integrations/document_loaders#all-document-loaders)

Document loaders provide a **standard interface** for reading data from different sources (such as Slack, Notion, or Google Drive) into LangChain’s [Document](https://reference.langchain.com/python/langchain-core/documents/base/Document) format.
This ensures that data can be handled consistently regardless of the source.All document loaders implement the [`BaseLoader`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader) interface.

## [​](https://docs.langchain.com/oss/python/integrations/document_loaders\#interface)  Interface

Each document loader may define its own parameters, but they share a common API:

- `load()` – Loads all documents at once.
- `lazy_load()` – Streams documents lazily, useful for large datasets.

Copy

```
from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(
    ...  # Integration-specific parameters here
)

# Load all documents
documents = loader.load()

# For large datasets, lazily load documents
for document in loader.lazy_load():
    print(document)
```

## [​](https://docs.langchain.com/oss/python/integrations/document_loaders\#by-category)  By category

### [​](https://docs.langchain.com/oss/python/integrations/document_loaders\#webpages)  Webpages

The below document loaders allow you to load webpages.

| Document Loader | Description | Package/API |
| --- | --- | --- |
| [Web](https://docs.langchain.com/oss/python/integrations/document_loaders/web_base) | Uses urllib and BeautifulSoup to load and parse HTML web pages | Package |
| [Unstructured](https://docs.langchain.com/oss/python/integrations/document_loaders/unstructured_file) | Uses Unstructured to load and parse web pages | Package |
| [RecursiveURL](https://docs.langchain.com/oss/python/integrations/document_loaders/recursive_url) | Recursively scrapes all child links from a root URL | Package |
| [Sitemap](https://docs.langchain.com/oss/python/integrations/document_loaders/sitemap) | Scrapes all pages on a given sitemap | Package |
| [Spider](https://docs.langchain.com/oss/python/integrations/document_loaders/spider) | Crawler and scraper that returns LLM-ready data | API |
| [Firecrawl](https://docs.langchain.com/oss/python/integrations/document_loaders/firecrawl) | API service that can be deployed locally | API |
| [Apify Dataset](https://docs.langchain.com/oss/python/integrations/document_loaders/apify_dataset) | Load documents from Apify datasets | API |
| [Docling](https://docs.langchain.com/oss/python/integrations/document_loaders/docling) | Uses Docling to load and parse web pages | Package |
| [Hyperbrowser](https://docs.langchain.com/oss/python/integrations/document_loaders/hyperbrowser) | Platform for running and scaling headless browsers, can be used to scrape/crawl any site | API |
| [AgentQL](https://docs.langchain.com/oss/python/integrations/document_loaders/agentql) | Web interaction and structured data extraction from any web page using an AgentQL query or a Natural Language prompt | API |

### [​](https://docs.langchain.com/oss/python/integrations/document_loaders\#pdfs)  PDFs

The below document loaders allow you to load PDF documents.

| Document Loader | Description | Package/API |
| --- | --- | --- |
| [PyPDF](https://docs.langchain.com/oss/python/integrations/document_loaders/pypdfloader) | Uses `pypdf` to load and parse PDFs | Package |
| [Unstructured](https://docs.langchain.com/oss/python/integrations/document_loaders/unstructured_file) | Uses Unstructured’s open source library to load PDFs | Package |
| [Amazon Textract](https://docs.langchain.com/oss/python/integrations/document_loaders/amazon_textract) | Uses AWS API to load PDFs | API |
| [MathPix](https://docs.langchain.com/oss/python/integrations/document_loaders/mathpix) | Uses MathPix to load PDFs | Package |
| [PDFPlumber](https://docs.langchain.com/oss/python/integrations/document_loaders/pdfplumber) | Load PDF files using PDFPlumber | Package |
| [PyPDFDirectry](https://docs.langchain.com/oss/python/integrations/document_loaders/pypdfdirectory) | Load a directory with PDF files | Package |
| [PyPDFium2](https://docs.langchain.com/oss/python/integrations/document_loaders/pypdfium2) | Load PDF files using PyPDFium2 | Package |
| [PyMuPDF](https://docs.langchain.com/oss/python/integrations/document_loaders/pymupdf) | Load PDF files using PyMuPDF | Package |
| [PyMuPDF4LLM](https://docs.langchain.com/oss/python/integrations/document_loaders/pymupdf4llm) | Load PDF content to Markdown using PyMuPDF4LLM | Package |
| [PDFMiner](https://docs.langchain.com/oss/python/integrations/document_loaders/pdfminer) | Load PDF files using PDFMiner | Package |
| [Upstage Document Parse Loader](https://docs.langchain.com/oss/python/integrations/document_loaders/upstage) | Load PDF files using UpstageDocumentParseLoader | Package |
| [Docling](https://docs.langchain.com/oss/python/integrations/document_loaders/docling) | Load PDF files using Docling | Package |
| [UnDatasIO](https://docs.langchain.com/oss/python/integrations/document_loaders/undatasio) | Load PDF files using UnDatasIO | Package |
| [OpenDataLoader PDF](https://docs.langchain.com/oss/python/integrations/document_loaders/opendataloader_pdf) | Load PDF files using OpenDataLoader PDF | Package |

### [​](https://docs.langchain.com/oss/python/integrations/document_loaders\#cloud-providers)  Cloud providers

The below document loaders allow you to load documents from your favorite cloud providers.

| Document Loader | Description | Partner Package | API reference |
| --- | --- | --- | --- |
| [AWS S3 Directory](https://docs.langchain.com/oss/python/integrations/document_loaders/aws_s3_directory) | Load documents from an AWS S3 directory | ❌ | [`S3DirectoryLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.s3_directory.S3DirectoryLoader.html) |
| [AWS S3 File](https://docs.langchain.com/oss/python/integrations/document_loaders/aws_s3_file) | Load documents from an AWS S3 file | ❌ | [`S3FileLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.s3_file.S3FileLoader.html) |
| [Azure AI Data](https://docs.langchain.com/oss/python/integrations/document_loaders/azure_ai_data) | Load documents from Azure AI services | ❌ | [`AzureAIDataLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.azure_ai_data.AzureAIDataLoader.html) |
| [Azure Blob Storage](https://docs.langchain.com/oss/python/integrations/document_loaders/azure_blob_storage) | Load documents from Azure Blob Storage | ✅ | [`AzureBlobStorageLoader`](https://reference.langchain.com/python/integrations/langchain_azure/storage/) |
| [Dropbox](https://docs.langchain.com/oss/python/integrations/document_loaders/dropbox) | Load documents from Dropbox | ❌ | [`DropboxLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html) |
| [Google Cloud Storage Directory](https://docs.langchain.com/oss/python/integrations/document_loaders/google_cloud_storage_directory) | Load documents from GCS bucket | ✅ | [`GCSDirectoryLoader`](https://python.langchain.com/api_reference/google_community/gcs_directory/langchain_google_community.gcs_directory.GCSDirectoryLoader.html) |
| [Google Cloud Storage File](https://docs.langchain.com/oss/python/integrations/document_loaders/google_cloud_storage_file) | Load documents from GCS file object | ✅ | [`GCSFileLoader`](https://python.langchain.com/api_reference/google_community/gcs_file/langchain_google_community.gcs_file.GCSFileLoader.html) |
| [Google Drive](https://docs.langchain.com/oss/python/integrations/document_loaders/google_drive) | Load documents from Google Drive (Google Docs only) | ✅ | [`GoogleDriveLoader`](https://python.langchain.com/api_reference/google_community/drive/langchain_google_community.drive.GoogleDriveLoader.html) |
| [Huawei OBS Directory](https://docs.langchain.com/oss/python/integrations/document_loaders/huawei_obs_directory) | Load documents from Huawei Object Storage Service Directory | ❌ | [`OBSDirectoryLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.obs_directory.OBSDirectoryLoader.html) |
| [Huawei OBS File](https://docs.langchain.com/oss/python/integrations/document_loaders/huawei_obs_file) | Load documents from Huawei Object Storage Service File | ❌ | [`OBSFileLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.obs_file.OBSFileLoader.html) |
| [Microsoft OneDrive](https://docs.langchain.com/oss/python/integrations/document_loaders/microsoft_onedrive) | Load documents from Microsoft OneDrive | ❌ | [`OneDriveLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.onedrive.OneDriveLoader.html) |
| [Microsoft SharePoint](https://docs.langchain.com/oss/python/integrations/document_loaders/microsoft_sharepoint) | Load documents from Microsoft SharePoint | ❌ | [`SharePointLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.sharepoint.SharePointLoader.html) |
| [Tencent COS Directory](https://docs.langchain.com/oss/python/integrations/document_loaders/tencent_cos_directory) | Load documents from Tencent Cloud Object Storage Directory | ❌ | [`TencentCOSDirectoryLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.tencent_cos_directory.TencentCOSDirectoryLoader.html) |
| [Tencent COS File](https://docs.langchain.com/oss/python/integrations/document_loaders/tencent_cos_file) | Load documents from Tencent Cloud Object Storage File | ❌ | [`TencentCOSFileLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.tencent_cos_file.TencentCOSFileLoader.html) |

### [​](https://docs.langchain.com/oss/python/integrations/document_loaders\#social-platforms)  Social platforms

The below document loaders allow you to load documents from different social media platforms.

| Document Loader | API reference |
| --- | --- |
| [Twitter](https://docs.langchain.com/oss/python/integrations/document_loaders/twitter) | [`TwitterTweetLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.twitter.TwitterTweetLoader.html) |
| [Reddit](https://docs.langchain.com/oss/python/integrations/document_loaders/reddit) | [`RedditPostsLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.reddit.RedditPostsLoader.html) |

### [​](https://docs.langchain.com/oss/python/integrations/document_loaders\#messaging-services)  Messaging services

The below document loaders allow you to load data from different messaging platforms.

| Document Loader | API reference |
| --- | --- |
| [Telegram](https://docs.langchain.com/oss/python/integrations/document_loaders/telegram) | [`TelegramChatFileLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.telegram.TelegramChatFileLoader.html) |
| [WhatsApp](https://docs.langchain.com/oss/python/integrations/document_loaders/whatsapp_chat) | [`WhatsAppChatLoader`](https://python.langchain.com/api_reference/community/chat_loaders/langchain_community.chat_loaders.whatsapp.WhatsAppChatLoader.html) |
| [Discord](https://docs.langchain.com/oss/python/integrations/document_loaders/discord) | [`DiscordChatLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.discord.DiscordChatLoader.html) |
| [Facebook Chat](https://docs.langchain.com/oss/python/integrations/document_loaders/facebook_chat) | [`FacebookChatLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.facebook_chat.FacebookChatLoader.html) |
| [Mastodon](https://docs.langchain.com/oss/python/integrations/document_loaders/mastodon) | [`MastodonTootsLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.mastodon.MastodonTootsLoader.html) |

### [​](https://docs.langchain.com/oss/python/integrations/document_loaders\#productivity-tools)  Productivity tools

The below document loaders allow you to load data from commonly used productivity tools.

| Document Loader | API reference |
| --- | --- |
| [Figma](https://docs.langchain.com/oss/python/integrations/document_loaders/figma) | [`FigmaFileLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.figma.FigmaFileLoader.html) |
| [Notion](https://docs.langchain.com/oss/python/integrations/document_loaders/notion) | [`NotionDirectoryLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.notion.NotionDirectoryLoader.html) |
| [Slack](https://docs.langchain.com/oss/python/integrations/document_loaders/slack) | [`SlackDirectoryLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.slack_directory.SlackDirectoryLoader.html) |
| [Quip](https://docs.langchain.com/oss/python/integrations/document_loaders/quip) | [`QuipLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.quip.QuipLoader.html) |
| [Trello](https://docs.langchain.com/oss/python/integrations/document_loaders/trello) | [`TrelloLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.trello.TrelloLoader.html) |
| [Roam](https://docs.langchain.com/oss/python/integrations/document_loaders/roam) | [`RoamLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.roam.RoamLoader.html) |
| [GitHub](https://docs.langchain.com/oss/python/integrations/document_loaders/github) | [`GithubFileLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.github.GithubFileLoader.html) |

### [​](https://docs.langchain.com/oss/python/integrations/document_loaders\#common-file-types)  Common file types

The below document loaders allow you to load data from common data formats.

| Document Loader | Data Type |
| --- | --- |
| [`CSVLoader`](https://docs.langchain.com/oss/python/integrations/document_loaders/csv) | CSV files |
| [`Unstructured`](https://docs.langchain.com/oss/python/integrations/document_loaders/unstructured_file) | Many file types (see [https://docs.unstructured.io/platform/supported-file-types](https://docs.unstructured.io/platform/supported-file-types)) |
| [`JSONLoader`](https://docs.langchain.com/oss/python/integrations/document_loaders/json) | JSON files |
| [`BSHTMLLoader`](https://docs.langchain.com/oss/python/integrations/document_loaders/bshtml) | HTML files |
| [`DoclingLoader`](https://docs.langchain.com/oss/python/integrations/document_loaders/docling) | Various file types (see [https://ds4sd.github.io/docling/](https://ds4sd.github.io/docling/)) |
| [`PolarisAIDataInsightLoader`](https://docs.langchain.com/oss/python/integrations/document_loaders/polaris_ai_datainsight) | Various file types (see [https://datainsight.polarisoffice.com/documentation?docType=doc\_extract](https://datainsight.polarisoffice.com/documentation?docType=doc_extract)) |

## [​](https://docs.langchain.com/oss/python/integrations/document_loaders\#all-document-loaders)  All document loaders

[**acreom** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/acreom) [**AgentQLLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/agentql) [**AirbyteLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/airbyte) [**Airtable** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/airtable) [**Alibaba Cloud MaxCompute** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/alibaba_cloud_maxcompute) [**Amazon Textract** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/amazon_textract) [**Apify Dataset** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/apify_dataset) [**ArxivLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/arxiv) [**AssemblyAI Audio Transcripts** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/assemblyai) [**AstraDB** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/astradb) [**Async Chromium** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/async_chromium) [**AsyncHtml** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/async_html) [**Athena** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/athena) [**AWS S3 Directory** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/aws_s3_directory) [**AWS S3 File** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/aws_s3_file) [**AZLyrics** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/azlyrics) [**Azure AI Data** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/azure_ai_data) [**Azure Blob Storage** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/azure_blob_storage) [**Azure AI Document Intelligence** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/azure_document_intelligence) [**BibTeX** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/bibtex) [**BiliBili** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/bilibili) [**Blackboard** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/blackboard) [**Blockchain** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/blockchain) [**Box** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/box) [**Brave Search** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/brave_search) [**Browserbase** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/browserbase) [**Browserless** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/browserless) [**BSHTMLLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/bshtml) [**Cassandra** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/cassandra) [**ChatGPT Data** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/chatgpt_loader) [**College Confidential** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/college_confidential) [**Concurrent Loader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/concurrent) [**Confluence** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/confluence) [**CoNLL-U** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/conll-u) [**Copy Paste** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/copypaste) [**Couchbase** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/couchbase) [**CSV** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/csv) [**Cube Semantic Layer** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/cube_semantic) [**Datadog Logs** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/datadog_logs) [**Dedoc** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/dedoc) [**Diffbot** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/diffbot) [**Discord** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/discord) [**Docling** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/docling) [**Docugami** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/docugami) [**Docusaurus** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/docusaurus) [**Dropbox** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/dropbox) [**Email** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/email) [**EPub** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/epub) [**Etherscan** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/etherscan) [**EverNote** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/evernote) [**Facebook Chat** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/facebook_chat) [**Fauna** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/fauna) [**Figma** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/figma) [**FireCrawl** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/firecrawl) [**Geopandas** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/geopandas) [**Git** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/git) [**GitBook** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/gitbook) [**GitHub** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/github) [**Glue Catalog** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/glue_catalog) [**Google AlloyDB for PostgreSQL** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_alloydb) [**Google BigQuery** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_bigquery) [**Google Bigtable** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_bigtable) [**Google Cloud SQL for SQL Server** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_cloud_sql_mssql) [**Google Cloud SQL for MySQL** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_cloud_sql_mysql) [**Google Cloud SQL for PostgreSQL** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_cloud_sql_pg) [**Google Cloud Storage Directory** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_cloud_storage_directory) [**Google Cloud Storage File** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_cloud_storage_file) [**Google Firestore in Datastore Mode** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_datastore) [**Google Drive** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_drive) [**Google El Carro for Oracle Workloads** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_el_carro) [**Google Firestore (Native Mode)** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_firestore) [**Google Memorystore for Redis** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_memorystore_redis) [**Google Spanner** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_spanner) [**Google Speech-to-Text** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/google_speech_to_text) [**Grobid** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/grobid) [**Gutenberg** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/gutenberg) [**Hacker News** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/hacker_news) [**Huawei OBS Directory** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/huawei_obs_directory) [**Huawei OBS File** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/huawei_obs_file) [**HuggingFace Dataset** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/hugging_face_dataset) [**HyperbrowserLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/hyperbrowser) [**iFixit** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/ifixit) [**Images** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/image) [**Image Captions** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/image_captions) [**IMSDb** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/imsdb) [**Iugu** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/iugu) [**Joplin** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/joplin) [**JSONLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/json) [**Jupyter Notebook** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/jupyter_notebook) [**Kinetica** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/kinetica) [**lakeFS** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/lakefs) [**LangSmith** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/langsmith) [**LarkSuite (FeiShu)** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/larksuite) [**LLM Sherpa** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/llmsherpa) [**Mastodon** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/mastodon) [**MathPixPDFLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/mathpix) [**MediaWiki Dump** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/mediawikidump) [**Merge Documents Loader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/merge_doc) [**MHTML** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/mhtml) [**Microsoft Excel** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/microsoft_excel) [**Microsoft OneDrive** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/microsoft_onedrive) [**Microsoft OneNote** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/microsoft_onenote) [**Microsoft PowerPoint** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/microsoft_powerpoint) [**Microsoft SharePoint** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/microsoft_sharepoint) [**Microsoft Word** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/microsoft_word) [**Near Blockchain** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/mintbase) [**Modern Treasury** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/modern_treasury) [**MongoDB** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/mongodb) [**Needle Document Loader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/needle) [**News URL** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/news) [**Notion DB** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/notion) [**Nuclia** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/nuclia) [**Obsidian** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/obsidian) [**OpenDataLoader PDF** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/opendataloader_pdf) [**Open Document Format (ODT)** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/odt) [**Open City Data** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/open_city_data) [**Oracle Autonomous Database** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/oracleadb_loader) [**Oracle AI Database** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/oracleai) [**Org-mode** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/org_mode) [**Outline Document Loader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/outline) [**PaddleOCR-VL** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/paddleocr_vl) [**Pandas DataFrame** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/pandas_dataframe) [**PDFMinerLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/pdfminer) [**PDFPlumber** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/pdfplumber) [**Pebblo Safe DocumentLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/pebblo) [**Polaris AI DataInsight** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/polaris_ai_datainsight) [**Polars DataFrame** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/polars_dataframe) [**Dell PowerScale** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/powerscale) [**Psychic** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/psychic) [**PubMed** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/pubmed) [**PyMuPDFLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/pymupdf) [**PyMuPDF4LLM** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/pymupdf4llm) [**PyPDFDirectoryLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/pypdfdirectory) [**PyPDFium2Loader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/pypdfium2) [**PyPDFLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/pypdfloader) [**PySpark** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/pyspark_dataframe) [**Quip** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/quip) [**ReadTheDocs Documentation** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/readthedocs_documentation) [**Recursive URL** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/recursive_url) [**Reddit** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/reddit) [**Roam** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/roam) [**Rockset** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/rockset) [**rspace** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/rspace) [**RSS Feeds** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/rss) [**RST** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/rst) [**scrapfly** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/scrapfly) [**ScrapingAnt** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/scrapingant) [**SingleStore** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/singlestore) [**Sitemap** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/sitemap) [**Slack** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/slack) [**Snowflake** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/snowflake) [**Soniox** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/soniox) [**Source Code** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/source_code) [**Spider** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/spider) [**Spreedly** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/spreedly) [**Stripe** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/stripe) [**Subtitle** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/subtitle) [**SurrealDB** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/surrealdb) [**Telegram** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/telegram) [**Tencent COS Directory** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/tencent_cos_directory) [**Tencent COS File** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/tencent_cos_file) [**TensorFlow Datasets** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/tensorflow_datasets) [**TiDB** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/tidb) [**2Markdown** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/tomarkdown) [**TOML** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/toml) [**Trello** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/trello) [**TSV** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/tsv) [**Twitter** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/twitter) [**UnDatasIO** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/undatasio) [**Unstructured** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/unstructured_file) [**UnstructuredMarkdownLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/unstructured_markdown) [**UnstructuredPDFLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/unstructured_pdfloader) [**Upstage** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/upstage) [**URL** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/url) [**Vsdx** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/vsdx) [**Weather** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/weather) [**WebBaseLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/web_base) [**WhatsApp Chat** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/whatsapp_chat) [**Wikipedia** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/wikipedia) [**UnstructuredXMLLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/xml) [**Xorbits Pandas DataFrame** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/xorbits) [**YouTube Audio** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/youtube_audio) [**YouTube Transcripts** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/youtube_transcript) [**YoutubeLoaderDL** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/yt_dlp) [**Yuque** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/yuque) [**ZeroxPDFLoader** \\
\\
View guide](https://docs.langchain.com/oss/python/integrations/document_loaders/zeroxpdfloader)

* * *

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

[Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

Was this page helpful?

YesNo

[Vector store integrations\\
\\
Previous](https://docs.langchain.com/oss/python/integrations/vectorstores) [Store integrations\\
\\
Next](https://docs.langchain.com/oss/python/integrations/stores)

Ctrl+I