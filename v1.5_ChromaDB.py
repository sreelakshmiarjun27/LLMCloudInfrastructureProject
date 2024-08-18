import chromadb
from langchain_openai import OpenAIEmbeddings
import os
import json

# Initialize ChromaDB client
client = chromadb.PersistentClient(path="db/")

# Delete existing collection if it exists
try:
    client.delete_collection("document_chunks")
except:
    pass

# Create a new collection
collection = client.create_collection("document_chunks")

# Initialize the OpenAI embeddings model with your API key
api_key = os.environ.get("OPENAI_API_KEY", "")
embeddings_model = OpenAIEmbeddings(api_key=api_key)

# Read the chunks from the file
chunks = []
with open("split_unstructured_data.txt", "r") as f:
    current_chunk = {"id": "", "content": "", "metadata": {}}
    for line in f:
        if line.startswith("Chunk "):
            if current_chunk["id"]:
                chunks.append(current_chunk)
            current_chunk = {"id": line.strip(), "content": "", "metadata": {}}
        elif line.startswith("Metadata:"):
            try:
                current_chunk["metadata"] = eval(line.replace("Metadata:", "").strip())
            except:
                current_chunk["metadata"] = {"default": "no_metadata"}
        elif line.startswith("Content:"):
            current_chunk["content"] = next(f).strip()
    if current_chunk["id"]:
        chunks.append(current_chunk)

# Print first 5 chunks for verification
print("Sample of first 5 chunks:")
for i, chunk in enumerate(chunks[:5]):
    print(f"Chunk {i+1}:")
    print(f"Content: {chunk['content'][:100]}...")  # First 100 characters
    print(f"Metadata: {chunk['metadata']}")
    print()

# Create embeddings for all chunks
all_texts = [chunk['content'] for chunk in chunks]
embeddings = embeddings_model.embed_documents(all_texts)

# Add chunks to the collection
for i, (chunk, embedding) in enumerate(zip(chunks, embeddings), start=1):
    unique_id = f"Chunk_{i}"
    try:
        collection.add(
            ids=[unique_id],
            embeddings=[embedding],
            documents=[chunk["content"]],
            metadatas=[chunk["metadata"] or {"default": "no_metadata"}]
        )
    except Exception as e:
        print(f"Error adding chunk {i}: {e}")

print(f"Added {len(chunks)} chunks to ChromaDB collection.")
print(f"Collection size: {collection.count()}")



print(f"Number of documents in collection: {collection.count()}")

