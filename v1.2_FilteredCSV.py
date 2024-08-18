# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:27:11 2024

@author: Sreelakshmi
"""

import pandas as pd

# Read the original CSV file
data = pd.read_csv('C:/Users/Sreelakshmi/OneDrive/Desktop/Project/part_1_0001.csv')

# Select the columns you want to keep
selected_columns = ['billingAccountId','billingAccountName','billingProfileId','billingProfileName','invoiceSectionId',
                    'invoiceSectionName','costCenter', 'servicePeriodEndDate', 'servicePeriodStartDate', 'date', 
                    'serviceFamily', 'productOrderId', 'productOrderName', 'consumedService', 'meterId', 'meterName', 'meterCategory', 
                    'meterSubCategory', 'meterRegion', 'ProductId', 'ProductName','SubscriptionId', 'subscriptionName', 'publisherType', 
                    'publisherName', 'resourceGroupName','ResourceId', 'resourceLocation', 'location', 'effectivePrice', 'quantity', 
                    'unitOfMeasure', 'chargeType', 'billingCurrency', 'pricingCurrency', 'costInBillingCurrency', 'costInPricingCurrency', 'costInUsd', 
                    'paygCostInBillingCurrency', 'paygCostInUsd', 'exchangeRatePricingToBilling', 'exchangeRateDate', 
                    'isAzureCreditEligible', 'serviceInfo2', 'additionalInfo', 'tags', 'PayGPrice', 
                    'frequency', 'term', 'pricingModel', 'unitPrice']

# Filter the data with the selected columns
filtered_data = data[selected_columns]

# Handle missing values
filtered_data = filtered_data.fillna('NaN')

# Convert date column format and handle missing dates
filtered_data['date'] = pd.to_datetime(filtered_data['date'], errors='coerce')
filtered_data['date'] = filtered_data['date'].fillna('Missing Date')

# Save the filtered data to a new CSV file
filtered_data.to_csv('filtered_invoice_data.csv', index=False)

# Load the filtered CSV data
filtered_data = pd.read_csv('filtered_invoice_data.csv')

# Convert the filtered data to neatly formatted text
formatted_data = "[" + ",\n".join([f"{row.to_dict()}" for index, row in filtered_data.iterrows()]) + "]"

# Save the formatted data to a local text file
with open('formatted_data.txt', 'w') as file:
    file.write(formatted_data)
