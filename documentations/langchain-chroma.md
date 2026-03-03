[Skip to main content](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#content-area)

[Docs by LangChain home page![light logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-dark-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=5babf1a1962208fd7eed942fa2432ecb)![dark logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-light-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=0bcd2a1f2599ed228bcedf0f535b45b1)](https://docs.langchain.com/)

![https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png](https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png)Open source

Search...

Ctrl K

Search...

Navigation

Chroma integration

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

- [Setup](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#setup)
- [Credentials](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#credentials)
- [Initialization](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#initialization)
- [Basic initialization](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#basic-initialization)
- [Running locally (In-Memory)](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#running-locally-in-memory)
- [Running locally (with data persistence)](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#running-locally-with-data-persistence)
- [Connecting to a chroma Server](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#connecting-to-a-chroma-server)
- [Chroma cloud](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#chroma-cloud)
- [Initialization from client](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#initialization-from-client)
- [Running locally (In-Memory)](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#running-locally-in-memory-2)
- [Running locally (with data persistence)](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#running-locally-with-data-persistence-2)
- [Connecting to a chroma Server](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#connecting-to-a-chroma-server-2)
- [Chroma cloud](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#chroma-cloud-2)
- [Access your chroma DB](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#access-your-chroma-db)
- [Create a chroma vectorstore](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#create-a-chroma-vectorstore)
- [Manage vector store](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#manage-vector-store)
- [Add items to vector store](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#add-items-to-vector-store)
- [Update items in vector store](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#update-items-in-vector-store)
- [Delete items from vector store](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#delete-items-from-vector-store)
- [Query vector store](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#query-vector-store)
- [Query directly](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#query-directly)
- [Similarity search](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#similarity-search)
- [Similarity search with score](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#similarity-search-with-score)
- [Search by vector](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#search-by-vector)
- [Other search methods](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#other-search-methods)
- [Query by turning into retriever](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#query-by-turning-into-retriever)
- [Usage for retrieval-augmented generation](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#usage-for-retrieval-augmented-generation)
- [API reference](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma#api-reference)

This notebook covers how to get started with the `Chroma` vector store.

> [Chroma](https://docs.trychroma.com/getting-started) is a AI-native open-source vector database focused on developer productivity and happiness. Chroma is licensed under Apache 2.0. View the full docs of `Chroma` at [this page](https://docs.trychroma.com/reference/py-collection), and find the API reference for the LangChain integration at [this page](https://python.langchain.com/api_reference/chroma/vectorstores/langchain_chroma.vectorstores.Chroma.html).

**Chroma Cloud**Chroma Cloud powers serverless vector and full-text search. It’s extremely fast, cost-effective, scalable and painless. Create a DB and try it out in under 30 seconds with $5 of free credits.[Get started with Chroma Cloud](https://trychroma.com/signup)

## [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#setup)  Setup

To access `Chroma` vector stores you’ll need to install the `langchain-chroma` integration package.

Copy

```
pip install -qU "langchain-chroma>=0.1.2"
```

### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#credentials)  Credentials

You can use the `Chroma` vector store without any credentials, simply installing the package above is enough!If you are a [Chroma Cloud](https://trychroma.com/signup) user, set your `CHROMA_TENANT`, `CHROMA_DATABASE`, and `CHROMA_API_KEY` environment variables.When you install the `chromadb` package you also get access to the Chroma CLI, which can set these for you. First, [login](https://docs.trychroma.com/docs/cli/login) via the CLI, and then use the [`connect` command](https://docs.trychroma.com/docs/cli/db):

Copy

```
chroma db connect [db_name] --env-file
```

If you want to get best in-class automated tracing of your model calls you can also set your [LangSmith](https://docs.langchain.com/langsmith/home) API key by uncommenting below:

Copy

```
os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
os.environ["LANGSMITH_TRACING"] = "true"
```

## [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#initialization)  Initialization

### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#basic-initialization)  Basic initialization

Below is a basic initialization, including the use of a directory to save the data locally.

Copy

```
# | output: false
# | echo: false
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
```

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#running-locally-in-memory)  Running locally (In-Memory)

You can get a Chroma server running in memory by simply instantiating a `Chroma` instance with a collection name and your embeddings provider:

Copy

```
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
)
```

If you don’t need data persistence, this is a great option for experimenting while building your AI application with LangChain.

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#running-locally-with-data-persistence)  Running locally (with data persistence)

You can provide the `persist_directory` argument to save your data across multiple runs of your program:

Copy

```
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",
)
```

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#connecting-to-a-chroma-server)  Connecting to a chroma Server

If you have a Chroma server running locally, or you have [deployed](https://docs.trychroma.com/guides/deploy/client-server-mode) one yourself, you can connect to it by providing the `host` argument.For example, you can start a Chroma server running locally with `chroma run`, and then connect it with `host='localhost'`:

Copy

```
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    host="localhost",
)
```

For other deployments you can use the `port`, `ssl`, and `headers` arguments to customize your connection.

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#chroma-cloud)  Chroma cloud

Chroma Cloud users can also build with LangChain. Provide your `Chroma` instance with your Chroma Cloud API key, tenant, and DB name:

Copy

```
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    chroma_cloud_api_key=os.getenv("CHROMA_API_KEY"),
    tenant=os.getenv("CHROMA_TENANT"),
    database=os.getenv("CHROMA_DATABASE"),
)
```

### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#initialization-from-client)  Initialization from client

You can also initialize from a `Chroma` client, which is particularly useful if you want easier access to the underlying database.

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#running-locally-in-memory-2)  Running locally (In-Memory)

Copy

```
import chromadb

client = chromadb.Client()
```

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#running-locally-with-data-persistence-2)  Running locally (with data persistence)

Copy

```
import chromadb

client = chromadb.PersistentClient(path="./chroma_langchain_db")
```

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#connecting-to-a-chroma-server-2)  Connecting to a chroma Server

For example, if you are running a Chroma server locally (using `chroma run`):

Copy

```
import chromadb

client = chromadb.HttpClient(host="localhost", port=8000, ssl=False)
```

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#chroma-cloud-2)  Chroma cloud

After setting your `CHROMA_API_KEY`, `CHROMA_TENANT`, and `CHROMA_DATABASE`, you can simply instantiate:

Copy

```
import chromadb

client = chromadb.CloudClient()
```

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#access-your-chroma-db)  Access your chroma DB

Copy

```
collection = client.get_or_create_collection("collection_name")
collection.add(ids=["1", "2", "3"], documents=["a", "b", "c"])
```

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#create-a-chroma-vectorstore)  Create a chroma vectorstore

Copy

```
vector_store_from_client = Chroma(
    client=client,
    collection_name="collection_name",
    embedding_function=embeddings,
)
```

## [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#manage-vector-store)  Manage vector store

Once you have created your vector store, we can interact with it by adding and deleting different items.

### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#add-items-to-vector-store)  Add items to vector store

We can add items to our vector store by using the `add_documents` function.

Copy

```
from uuid import uuid4

from langchain_core.documents import Document

document_1 = Document(
    page_content="I had chocolate chip pancakes and scrambled eggs for breakfast this morning.",
    metadata={"source": "tweet"},
    id=1,
)

document_2 = Document(
    page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
    metadata={"source": "news"},
    id=2,
)

document_3 = Document(
    page_content="Building an exciting new project with LangChain - come check it out!",
    metadata={"source": "tweet"},
    id=3,
)

document_4 = Document(
    page_content="Robbers broke into the city bank and stole $1 million in cash.",
    metadata={"source": "news"},
    id=4,
)

document_5 = Document(
    page_content="Wow! That was an amazing movie. I can't wait to see it again.",
    metadata={"source": "tweet"},
    id=5,
)

document_6 = Document(
    page_content="Is the new iPhone worth the price? Read this review to find out.",
    metadata={"source": "website"},
    id=6,
)

document_7 = Document(
    page_content="The top 10 soccer players in the world right now.",
    metadata={"source": "website"},
    id=7,
)

document_8 = Document(
    page_content="LangGraph is the best framework for building stateful, agentic applications!",
    metadata={"source": "tweet"},
    id=8,
)

document_9 = Document(
    page_content="The stock market is down 500 points today due to fears of a recession.",
    metadata={"source": "news"},
    id=9,
)

document_10 = Document(
    page_content="I have a bad feeling I am going to get deleted :(",
    metadata={"source": "tweet"},
    id=10,
)

documents = [\
    document_1,\
    document_2,\
    document_3,\
    document_4,\
    document_5,\
    document_6,\
    document_7,\
    document_8,\
    document_9,\
    document_10,\
]
uuids = [str(uuid4()) for _ in range(len(documents))]

vector_store.add_documents(documents=documents, ids=uuids)
```

### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#update-items-in-vector-store)  Update items in vector store

Now that we have added documents to our vector store, we can update existing documents by using the `update_documents` function.

Copy

```
updated_document_1 = Document(
    page_content="I had chocolate chip pancakes and fried eggs for breakfast this morning.",
    metadata={"source": "tweet"},
    id=1,
)

updated_document_2 = Document(
    page_content="The weather forecast for tomorrow is sunny and warm, with a high of 82 degrees.",
    metadata={"source": "news"},
    id=2,
)

vector_store.update_document(document_id=uuids[0], document=updated_document_1)
# You can also update multiple documents at once
vector_store.update_documents(
    ids=uuids[:2], documents=[updated_document_1, updated_document_2]
)
```

### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#delete-items-from-vector-store)  Delete items from vector store

We can also delete items from our vector store as follows:

Copy

```
vector_store.delete(ids=uuids[-1])
```

## [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#query-vector-store)  Query vector store

Once your vector store has been created and the relevant documents have been added you will most likely wish to query it during the running of your chain or agent.

### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#query-directly)  Query directly

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#similarity-search)  Similarity search

Performing a simple similarity search can be done as follows:

Copy

```
results = vector_store.similarity_search(
    "LangChain provides abstractions to make working with LLMs easy",
    k=2,
    filter={"source": "tweet"},
)
for res in results:
    print(f"* {res.page_content} [{res.metadata}]")
```

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#similarity-search-with-score)  Similarity search with score

If you want to execute a similarity search and receive the corresponding scores you can run:

Copy

```
results = vector_store.similarity_search_with_score(
    "Will it be hot tomorrow?", k=1, filter={"source": "news"}
)
for res, score in results:
    print(f"* [SIM={score:3f}] {res.page_content} [{res.metadata}]")
```

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#search-by-vector)  Search by vector

You can also search by vector:

Copy

```
results = vector_store.similarity_search_by_vector(
    embedding=embeddings.embed_query("I love green eggs and ham!"), k=1
)
for doc in results:
    print(f"* {doc.page_content} [{doc.metadata}]")
```

#### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#other-search-methods)  Other search methods

There are a variety of other search methods that are not covered in this notebook, such as MMR search. For a full list of the search abilities available for `Chroma` check out the [API reference](https://python.langchain.com/api_reference/chroma/vectorstores/langchain_chroma.vectorstores.Chroma.html).

### [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#query-by-turning-into-retriever)  Query by turning into retriever

You can also transform the vector store into a retriever for easier usage in your chains. For more information on the different search types and kwargs you can pass, please visit the API reference [here](https://python.langchain.com/api_reference/chroma/vectorstores/langchain_chroma.vectorstores.Chroma.html#langchain_chroma.vectorstores.Chroma.as_retriever).

Copy

```
retriever = vector_store.as_retriever(
    search_type="mmr", search_kwargs={"k": 1, "fetch_k": 5}
)
retriever.invoke("Stealing from the bank is a crime", filter={"source": "news"})
```

## [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#usage-for-retrieval-augmented-generation)  Usage for retrieval-augmented generation

For guides on how to use this vector store for retrieval-augmented generation (RAG), see the following sections:

- [Tutorials](https://docs.langchain.com/oss/python/langchain/rag)
- [How-to: Question and answer with RAG](https://python.langchain.com/docs/how_to/#qa-with-rag)
- [Retrieval conceptual docs](https://python.langchain.com/docs/concepts/retrieval)

* * *

## [​](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma\#api-reference)  API reference

For detailed documentation of all `Chroma` vector store features and configurations head to the API reference: [python.langchain.com/api\_reference/chroma/vectorstores/langchain\_chroma.vectorstores.Chroma.html](https://python.langchain.com/api_reference/chroma/vectorstores/langchain_chroma.vectorstores.Chroma.html)

* * *

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/vectorstores/chroma.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

[Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

Was this page helpful?

YesNo

Ctrl+I