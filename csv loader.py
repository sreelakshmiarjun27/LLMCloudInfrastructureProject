# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:18:04 2024

@author: Sreelakshmi
"""

from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders.csv_loader import UnstructuredCSVLoader


# Load the CSV data using CSVLoader
loader = CSVLoader(file_path="filtered_invoice_data.csv")
data = loader.load()

# Print each row with metadata on one line and page_content on a new line
for document in data:
    print(f"Metadata: {document.metadata}")
    print(f"Page Content:\n{document.page_content}\n")



loader = CSVLoader(
    file_path="filtered_invoice_data.csv",
    csv_args={
        "delimiter": ",",
        "quotechar": '"',
        "fieldnames": ["MLB Team", "Payroll in millions", "Wins"],
    },
)

data = loader.load()

print(data)

loader = CSVLoader(file_path="filtered_invoice_data.csv", source_column="billingAccountId")

data = loader.load()

# Print each row with metadata on one line and page_content on a new line
for document in data:
    print(f"Metadata: {document.metadata}")
    print(f"Page Content:\n{document.page_content}\n")
    
loader = UnstructuredCSVLoader(
    file_path="filtered_invoice_data.csv", mode="elements"
)
docs = loader.load()

print(docs[0].metadata["text_as_html"])