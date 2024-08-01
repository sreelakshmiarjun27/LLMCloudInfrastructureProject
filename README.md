# Cloud Information Chatbot

## Overview
This project implements a chatbot designed to answer queries about cloud usage, billing, and other cloud-related information. The system uses a Retrieval-Augmented Generation (RAG) approach, combining information retrieval with advanced large language models to provide accurate and context-aware responses.

## Features
- CSV data ingestion and processing
- Text chunking for efficient processing
- Embedding generation using OpenAI models
- Vector storage and retrieval with ChromaDB
- Natural language query processing
- Response generation using GPT model-gpt-4o
- User-friendly interface with Streamlit

## Workflow
1. Data Ingestion: CSV files are loaded using LangChain's CSVLoader.
2. Text Processing: Documents are split into chunks using RecursiveCharacterTextSplitter.
3. Embedding Generation: Text chunks are converted to embeddings using OpenAI's embedding model.
4. Vector Storage: Embeddings are stored in ChromaDB for efficient retrieval.
5. Query Processing: User queries are embedded and used to retrieve relevant context.
6. Response Generation: Retrieved context and query are sent to GPT model(gpt-4o)for answer generation.
7. User Interface: Responses are displayed through a Streamlit-based interface.

## Requirements
- Python 3.11.3
- LangChain 
- OpenAI API
- ChromaDB
- Streamlit

## Installation
pip install langchain openai chromadb streamlit
