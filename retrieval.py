import os
import chromadb
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

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
retriever = langchain_chroma.as_retriever(search_kwargs={"k": 5})

# Initialize the language model
llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

# Create a custom prompt template
prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Answer:"""
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

# Create the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)

def ask_question(question):
    result = qa_chain({"query": question})
    return result["result"], result["source_documents"]

# Check database contents
print("Checking database contents:")
sample_results = langchain_chroma.similarity_search("billingAccountId", k=3)
for doc in sample_results:
    print(doc.page_content[:200])  # Print first 200 characters
    print("-" * 50)

# Main loop
while True:
    user_question = input("Ask a question (or type 'quit' to exit): ")
    if user_question.lower() == 'quit':
        break

    answer, sources = ask_question(user_question)
    
    print("\nAnswer:", answer)
    print("\nSources:")
    for i, doc in enumerate(sources, 1):
        print(f"Source {i}:")
        print(doc.page_content[:200])  # Print first 200 characters
        print("-" * 50)

print("Thank you for using the QA system!")
