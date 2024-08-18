# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:10:07 2024

@author: Sreelakshmi
"""
import os
import openai

# Retrieve the OpenAI API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Check if the API key is available
if api_key is None:
 print("Please set the OPENAI_API_KEY environment variable.")
else:
# Set up the OpenAI API client with the obtained key
 openai.api_key = api_key

# Define your prompt here
prompt = "Your customized prompt goes here."

# Use the GPT-4o model with chat completion endpoint
response = openai.ChatCompletion.create(
model="gpt-4o", # Update the model name to use GPT-4o
messages=[
{"role": "system", "content": "You are a cloud infrastructure expert."},
{"role": "user", "content": ""}
]
)

print(response.choices[0].message['content'])
