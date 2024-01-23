import pandas as pd

# Load transaction data
transactions = pd.read_csv("transactions.csv")

# Get spending by category
spending_by_category = transactions.groupby('category')['amount'].sum()

# Identify top spending categories
top_categories = spending_by_category.sort_values(ascending=False).head(3)
