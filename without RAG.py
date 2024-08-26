import os
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import logging
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up OpenAI API key
api_key = os.environ.get("OPENAI_API_KEY", "")

# Initialize the language model
llm = ChatOpenAI(model_name="gpt-4o")

# Create a custom prompt template
prompt_template = """
You are CloudBot, a helpful assistant. Answer the following question to best of your knowledge.

Question: {question}

Answer: """

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["question"]
)

# Create the LLMChain
llm_chain = LLMChain(llm=llm, prompt=PROMPT)

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
        
        # A response is generated  
        result = llm_chain.run(question=question)
        
        logger.info(f"Generated answer: {result}")
        return result, ""
    except Exception as e:
        logger.error(f"Error in ask_question: {str(e)}", exc_info=True)
        return f"An error occurred: {str(e)}", ""

# This function can be called from the comparison program
def get_answer(question):
    return ask_question(question)

