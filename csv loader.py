# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:18:04 2024

@author: Sreelakshmi
"""

from langchain_community.document_loaders.csv_loader import CSVLoader

# Function to load CSV data with specific fieldnames
def load_csv_with_specific_fieldnames(file_path, fieldnames):
    loader = CSVLoader(file_path=file_path, csv_args={"fieldnames": fieldnames})
    return loader.load()

# Load the CSV data using CSVLoader
loader = CSVLoader(file_path="filtered_invoice_data.csv")
data = loader.load()

# Print each row with metadata on one line and page_content on a new line
for document in data:
    print(f"Metadata: {document.metadata}")
    print(f"Page Content:\n{document.page_content}\n")

# Load the CSV data using CSVLoader with specific fieldnames
data_specific_fieldnames = load_csv_with_specific_fieldnames("filtered_invoice_data.csv",
    ['billingAccountId','billingAccountName','billingProfileId','billingProfileName','invoiceSectionId',
    'invoiceSectionName','costCenter', 'servicePeriodEndDate', 'servicePeriodStartDate', 'date',
    'serviceFamily', 'productOrderId', 'productOrderName', 'consumedService', 'meterId', 'meterName', 'meterCategory',
    'meterSubCategory', 'meterRegion', 'ProductId', 'ProductName','SubscriptionId', 'subscriptionName', 'publisherType',
    'publisherName', 'resourceGroupName','ResourceId', 'resourceLocation', 'location', 'effectivePrice', 'quantity',
    'unitOfMeasure', 'chargeType', 'billingCurrency', 'pricingCurrency', 'costInBillingCurrency', 'costInPricingCurrency', 'costInUsd',
    'paygCostInBillingCurrency', 'paygCostInUsd', 'exchangeRatePricingToBilling', 'exchangeRateDate',
    'isAzureCreditEligible', 'serviceInfo2', 'additionalInfo', 'tags', 'PayGPrice',
    'frequency', 'term', 'pricingModel', 'unitPrice']
)

# Print the second set of data with metadata and page content
for document in data_specific_fieldnames:
    print(f"Metadata: {document.metadata}")
    print(f"Page Content:\n{document.page_content}\n")

# Load the data using CSVLoader with source column as "billingAccountId"
loader = CSVLoader(file_path="filtered_invoice_data.csv", source_column="billingAccountId")
data_source_column = loader.load()

# Store the data with source column in a local file
output_file_source_column = "output_data_source_column.txt"
with open(output_file_source_column, "w") as file:
    for document in data_source_column:
        file.write(f"Metadata: {document.metadata}\n")
        file.write(f"Page Content:\n{document.page_content}\n\n")
