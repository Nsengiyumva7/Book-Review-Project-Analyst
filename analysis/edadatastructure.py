"""
Task 2 EDA –  Understanding Dataset Structure & Data Types
Project: Book Reviews Analysis
"""

import pandas as pd

# =============================
# 1. Load Dataset
# =============================
file_path = "data/raw_books.csv"
df = pd.read_csv(file_path)

print("Dataset loaded successfully.\n")

# =============================
# 2. Basic Shape Information
# =============================
print("Dataset Shape:")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}\n")

# =============================
# 3. Column Names
# =============================
print("Column Names:")
for col in df.columns:
    print(f"- {col}")
print()

# =============================
# 4. Data Types & Non-Null Counts
# =============================
print("Dataset Info:")
df.info()
print()

# =============================
# 5. Preview Data
# =============================
print("First 5 Rows:")
print(df.head())
print("\nLast 5 Rows:")
print(df.tail())
print()

# =============================
# 6. Missing Values Check
# =============================
print("Missing Values per Column:")
missing_values = df.isnull().sum().sort_values(ascending=False)
print(missing_values)
print()

# =============================
# 7. Unique Value Counts (Categorical Insight)
# =============================
print("Unique Value Counts (Selected Columns):")
for col in df.columns:
    if df[col].dtype == "object":
        print(f"{col}: {df[col].nunique()} unique values")
print()

# =============================
# 8. Initial Observations (Manual Notes)
# =============================
# - Identify columns that should be numeric but are objects
# - Check for suspicious missing values
# - Look for unusually high cardinality columns (e.g., titles)


# =============================
#  errors occured (Manual Notes)
# =============================

# - prices that should be numeric but are objects.
# - ratings should be numeric or ordinal.
# - Currency symbol this (£) not (Â£).
