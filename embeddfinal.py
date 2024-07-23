# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:35:27 2024

@author: Sreelakshmi
"""

from langchain_openai import OpenAIEmbeddings
import os
import json

# Read the contents of the split_unstructured_data.txt file
with open("split_unstructured_data.txt") as f:
    file_content = f.read()

# Initialize the OpenAI embeddings model with your API key
api_key = os.environ.get("OPENAI_API_KEY", "")  # It's a good practice to store API keys in environment variables
embeddings_model = OpenAIEmbeddings(api_key=api_key)

# Embed the contents of the file
embeddings = embeddings_model.embed_documents([file_content])

# Save the embeddings to a JSON file
output_file = "embeddings.json"

with open(output_file, "w") as output_f:
    json.dump(embeddings, output_f)

print("Embeddings saved to embeddings.json file.")