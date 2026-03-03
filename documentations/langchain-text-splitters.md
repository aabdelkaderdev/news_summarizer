# langchain-text-splitters

## Description

# 🦜✂️ LangChain Text Splitters

[![PyPI - Version](https://img.shields.io/pypi/v/langchain-text-splitters?label=%20)](https://pypi.org/project/langchain-text-splitters/#history)[![PyPI - License](https://img.shields.io/pypi/l/langchain-text-splitters)](https://opensource.org/licenses/MIT)[![PyPI - Downloads](https://img.shields.io/pepy/dt/langchain-text-splitters)](https://pypistats.org/packages/langchain-text-splitters)[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/langchain.svg?style=social&label=Follow%20%40LangChain)](https://x.com/langchain)

Looking for the JS/TS version? Check out [LangChain.js](https://github.com/langchain-ai/langchainjs).

## Quick Install

```
pip install langchain-text-splitters
```

Copy

## 🤔 What is this?

LangChain Text Splitters contains utilities for splitting into chunks a wide variety of text documents.

## 📖 Documentation

For full documentation, see the [API reference](https://reference.langchain.com/python/langchain_text_splitters/).

## 📕 Releases & Versioning

See our [Releases](https://docs.langchain.com/oss/python/release-policy) and [Versioning](https://docs.langchain.com/oss/python/versioning) policies.

We encourage pinning your version to a specific version in order to avoid breaking your CI when we publish new tests. We recommend upgrading to the latest version periodically to make sure you have the latest tests.

Not pinning your version will ensure you always have the latest tests, but it may also break your CI if we introduce tests that your integration doesn't pass.

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

For detailed information on how to contribute, see the [Contributing Guide](https://docs.langchain.com/oss/python/contributing/overview).

## Classes

[Class **TextSplitter**\\
\\
Interface for splitting text into chunks.](https://reference.langchain.com/python/langchain-text-splitters/base/TextSplitter) [Class **TokenTextSplitter**\\
\\
Splitting text to tokens using model tokenizer.](https://reference.langchain.com/python/langchain-text-splitters/base/TokenTextSplitter) [Class **Language**\\
\\
Enum of the programming languages.](https://reference.langchain.com/python/langchain-text-splitters/base/Language) [Class **Tokenizer**\\
\\
Tokenizer data class.](https://reference.langchain.com/python/langchain-text-splitters/base/Tokenizer) [Class **MarkdownTextSplitter**\\
\\
Attempts to split the text along Markdown-formatted headings.](https://reference.langchain.com/python/langchain-text-splitters/markdown/MarkdownTextSplitter) [Class **MarkdownHeaderTextSplitter**\\
\\
Splitting markdown files based on specified headers.](https://reference.langchain.com/python/langchain-text-splitters/markdown/MarkdownHeaderTextSplitter) [Class **LineType**\\
\\
Line type as `TypedDict`.](https://reference.langchain.com/python/langchain-text-splitters/markdown/LineType) [Class **HeaderType**\\
\\
Header type as `TypedDict`.](https://reference.langchain.com/python/langchain-text-splitters/markdown/HeaderType) [Class **ExperimentalMarkdownSyntaxTextSplitter**\\
\\
An experimental text splitter for handling Markdown syntax.](https://reference.langchain.com/python/langchain-text-splitters/markdown/ExperimentalMarkdownSyntaxTextSplitter) [Class **ElementType**\\
\\
Element type as typed dict.](https://reference.langchain.com/python/langchain-text-splitters/html/ElementType) [Class **HTMLHeaderTextSplitter**\\
\\
Split HTML content into structured Documents based on specified headers.](https://reference.langchain.com/python/langchain-text-splitters/html/HTMLHeaderTextSplitter) [Class **HTMLSectionSplitter**\\
\\
Splitting HTML files based on specified tag and font sizes.](https://reference.langchain.com/python/langchain-text-splitters/html/HTMLSectionSplitter) [Class **HTMLSemanticPreservingSplitter**\\
\\
Split HTML content preserving semantic structure.](https://reference.langchain.com/python/langchain-text-splitters/html/HTMLSemanticPreservingSplitter) [Class **JSFrameworkTextSplitter**\\
\\
Text splitter that handles React (JSX), Vue, and Svelte code.](https://reference.langchain.com/python/langchain-text-splitters/jsx/JSFrameworkTextSplitter) [Class **PythonCodeTextSplitter**\\
\\
Attempts to split the text along Python syntax.](https://reference.langchain.com/python/langchain-text-splitters/python/PythonCodeTextSplitter) [Class **KonlpyTextSplitter**\\
\\
Splitting text using Konlpy package.](https://reference.langchain.com/python/langchain-text-splitters/konlpy/KonlpyTextSplitter) [Class **CharacterTextSplitter**\\
\\
Splitting text that looks at characters.](https://reference.langchain.com/python/langchain-text-splitters/character/CharacterTextSplitter) [Class **RecursiveCharacterTextSplitter**\\
\\
Splitting text by recursively look at characters.](https://reference.langchain.com/python/langchain-text-splitters/character/RecursiveCharacterTextSplitter) [Class **SentenceTransformersTokenTextSplitter**\\
\\
Splitting text to tokens using sentence model tokenizer.](https://reference.langchain.com/python/langchain-text-splitters/sentence_transformers/SentenceTransformersTokenTextSplitter) [Class **RecursiveJsonSplitter**\\
\\
Splits JSON data into smaller, structured chunks while preserving hierarchy.](https://reference.langchain.com/python/langchain-text-splitters/json/RecursiveJsonSplitter) [Class **LatexTextSplitter**\\
\\
Attempts to split the text along Latex-formatted layout elements.](https://reference.langchain.com/python/langchain-text-splitters/latex/LatexTextSplitter) [Class **NLTKTextSplitter**\\
\\
Splitting text using NLTK package.](https://reference.langchain.com/python/langchain-text-splitters/nltk/NLTKTextSplitter) [Class **SpacyTextSplitter**\\
\\
Splitting text using Spacy package.](https://reference.langchain.com/python/langchain-text-splitters/spacy/SpacyTextSplitter)

## Functions

[Function **split\_text\_on\_tokens**\\
\\
Split incoming text and return chunks using tokenizer.](https://reference.langchain.com/python/langchain-text-splitters/base/split_text_on_tokens)

## Modules

[Module **langchain\_text\_splitters**\\
\\
Text Splitters are classes for splitting text.](https://reference.langchain.com/python/langchain-text-splitters/langchain_text_splitters) [Module **base**\\
\\
Text splitter base interface.](https://reference.langchain.com/python/langchain-text-splitters/base) [Module **markdown**\\
\\
Markdown text splitters.](https://reference.langchain.com/python/langchain-text-splitters/markdown) [Module **html**\\
\\
HTML text splitters.](https://reference.langchain.com/python/langchain-text-splitters/html) [Module **jsx**\\
\\
JavaScript framework text splitter.](https://reference.langchain.com/python/langchain-text-splitters/jsx) [Module **python**\\
\\
Python code text splitter.](https://reference.langchain.com/python/langchain-text-splitters/python) [Module **konlpy**\\
\\
Konlpy text splitter.](https://reference.langchain.com/python/langchain-text-splitters/konlpy) [Module **character**\\
\\
Character text splitters.](https://reference.langchain.com/python/langchain-text-splitters/character) [Module **sentence\_transformers**\\
\\
Sentence transformers text splitter.](https://reference.langchain.com/python/langchain-text-splitters/sentence_transformers) [Module **json**\\
\\
JSON text splitter.](https://reference.langchain.com/python/langchain-text-splitters/json) [Module **latex**\\
\\
Latex text splitter.](https://reference.langchain.com/python/langchain-text-splitters/latex) [Module **nltk**\\
\\
NLTK text splitter.](https://reference.langchain.com/python/langchain-text-splitters/nltk) [Module **spacy**\\
\\
Spacy text splitter.](https://reference.langchain.com/python/langchain-text-splitters/spacy)

⌘I

## LangChain Assistant

NewHistory

Ask a question to get started

`Enter` to send• `Shift+Enter` new line