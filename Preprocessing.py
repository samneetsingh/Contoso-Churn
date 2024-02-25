import pandas as pd
import numpy as np
import os

# Load the data
contact = pd.read_csv('Contact.csv')
customerLoyalty = pd.read_csv('Customer-Loyalty.csv')
subscriptionHistory = pd.read_csv('SubscriptionHistoryContoso.csv')
reviews = pd.read_csv('WebsiteReviews_LinkedToEcommerceContacts.csv')

# Fix the naming of primary key / foreign key
subscriptionHistory.rename(columns={'CustomerID': 'ContactId'}, inplace=True)
reviews.rename(columns={'UserId': 'ContactId'}, inplace=True)

# Merge the data
data = pd.merge(contact, customerLoyalty, on='ContactId', how='left')
data = pd.merge(data, subscriptionHistory, on='ContactId', how='left')
data = pd.merge(data, reviews, on='ContactId', how='left')

print(data.columns)
print(data.head())
