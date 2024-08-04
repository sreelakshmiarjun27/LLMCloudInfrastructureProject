import os
import chromadb
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import logging
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up OpenAI API key
api_key = os.environ.get("OPENAI_API_KEY", "")

# Initialize the embedding model
embeddings = OpenAIEmbeddings()

# Initialize ChromaDB client
client = chromadb.PersistentClient(path="db/")

# Get the existing collection
collection = client.get_collection("document_chunks")

# Create a Langchain Chroma wrapper
langchain_chroma = Chroma(
    client=client,
    collection_name="document_chunks",
    embedding_function=embeddings
)

# Create a retriever from the Chroma database
retriever = langchain_chroma.as_retriever(search_kwargs={"k": 5})  # Fetch the top 5 relevant chunks

# Initialize the language model
llm = ChatOpenAI(model_name="gpt-4", temperature=0)

# Create a custom prompt template
prompt_template = """
You are CloudBot, a helpful assistant. Your knowledge comes from the information provided in the context below. Use all the information available in the context to answer the question thoroughly.

Use the following pieces of context to answer the question at the end. If the information needed to answer the question is not present in the context, say that you don't have enough information to answer accurately.

Context: {context}

Question: {question}

Answer: """

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# Create the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)

def preprocess_text(text):
    # Tokenize
    tokens = word_tokenize(text.lower())
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

def ask_question(question):
    try:
        logger.info(f"Received question: {question}")
        
        # Retrieve relevant chunks using the retriever
        retrieved_chunks = retriever.get_relevant_documents(question)

        # Combine all relevant chunk texts into a single context
        combined_context = " ".join([chunk.page_content for chunk in retrieved_chunks])

        # Generate a response using the combined context
        result = qa_chain({
            "query": question,
            "context": combined_context
        })
        
        logger.info(f"Generated answer: {result['result']}")
        return result["result"], combined_context
    except Exception as e:
        logger.error(f"Error in ask_question: {str(e)}", exc_info=True)
        return f"An error occurred: {str(e)}", ""

# This function can be called from the Streamlit app
def get_answer(question):
    return ask_question(question)