
from langchain_text_splitters import RecursiveCharacterTextSplitter
import json

# Read the document
with open("output_data_final.txt") as f:
    final_unstructured_data = f.read()

# Define a custom split function
def custom_split(text):
    # Split the text into individual JSON objects
    objects = text.strip().split('\n\n')
    return [obj.strip() for obj in objects if obj.strip()]

# Create a custom text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # Increased chunk size
    chunk_overlap=0,  # No overlap needed for JSON objects
    length_function=len,
    separators=["\n\n"]  # Split on double newlines
)

# Split the document into chunks
texts = text_splitter.create_documents([final_unstructured_data])

# Store the split chunks into a new file
output_file = "split_unstructured_data.txt"
with open(output_file, 'w') as f:
    for i, text in enumerate(texts):
        # Parse the JSON content
        try:
            content = json.loads(text.page_content)
        except json.JSONDecodeError:
            content = text.page_content  # If it's not valid JSON, use as is

        f.write(f"Chunk {i+1}\n")
        f.write(f"Metadata: {text.metadata}\n")
        f.write(f"Content:\n{json.dumps(content, indent=2)}\n\n")

print(f"The split data has been written to {output_file}")