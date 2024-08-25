# Cloud Chatbot

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
- Evaluation of model performance and metrics
- Comparison between RAG and non-RAG chatbots

## Workflow
1. Data Ingestion: CSV files are loaded using LangChain's CSVLoader.
2. Text Processing: Documents are split into chunks using RecursiveCharacterTextSplitter.
3. Embedding Generation: Text chunks are converted to embeddings using OpenAI's embedding model.
4. Vector Storage: Embeddings are stored in ChromaDB for efficient retrieval.
5. Query Processing: User queries are embedded and used to retrieve relevant context.
6. Response Generation: Retrieved context and query are sent to GPT model(gpt-4o)for answer generation.
7. User Interface: Responses are displayed through a Streamlit-based interface.

## Modules
metrics.py: Contains functions for asking questions, computing evaluation metrics (accuracy, confidence score, context relevance, answer conciseness, response time), and saving results in JSON format.
plot_performance.py: Generates radar charts to visualize performance metrics saved in JSON format. It creates visual representations of user evaluation metrics to assess chatbot performance.
model_evaluation.py: Evaluates different models against a set of predefined questions to analyze response time, tokens used, and response length. This module provides comparative analysis of various language models.
plot.py: Loads the evaluation results and plots average metrics for different models using bar graphs, helping visualize differences in performance.
without_RAG.py: Implements a non-RAG chatbot that uses basic input-output processing without external retrieval systems. It includes text preprocessing capabilities to improve input handling.
compare_chatbots.py: Compares the performance of RAG-based and non-RAG chatbots, calculating the BLEU score to measure response similarity and timing for both approaches.

## Requirements
- Python 3.11.3
- LangChain 
- OpenAI API
- ChromaDB
- Streamlit
- NLTK
- matplotlib

## Installation
pip install langchain openai chromadb streamlit nltk matplotlib

## Usage
-Ensure the OpenAI API key is set in your environment: export OPENAI_API_KEY='your_api_key'.
-Prepare the CSV data and place it in the appropriate directory for ingestion.
-Execute the chatbot module to start interacting with it, querying for cloud-related information.
-Use the evaluation and plotting modules to analyze and visualize chatbot performance.

## Saving Results
-Results are saved in JSON format for further analysis. 
-The performance metrics and evaluation details are stored in files such as chatbot_results.json, results.json, and chatbot_comparison_results.json.

## Conclusion
This Cloud Information Chatbot is designed to enhance user interaction with cloud infrastructure by providing accurate, context-based answers while enabling seamless evaluation of various gpt models.


