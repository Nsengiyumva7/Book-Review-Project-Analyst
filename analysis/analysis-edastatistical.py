"""
Task 2 EDA –  Statistical Analysis & Distributions
Project: Book Reviews Analysis
"""

import pandas as pd

# =============================
# 1. Load Cleaned Dataset
# =============================
df = pd.read_csv("data/eda-cleaned_books.csv")

print("Dataset loaded for statistical analysis.\n")

# =============================
# 2. Descriptive Statistics
# =============================
print("Descriptive Statistics:")
print(df[["price", "rating"]].describe())
print()

# =============================
# 3. Central Tendency
# =============================
print("Central Tendency:")
print(f"Mean Price: {df['price'].mean():.2f}")
print(f"Median Price: {df['price'].median():.2f}")
print(f"Mode Price: {df['price'].mode().iloc[0]:.2f}")

print(f"Mean Rating: {df['rating'].mean():.2f}")
print(f"Median Rating: {df['rating'].median():.2f}")
print(f"Mode Rating: {df['rating'].mode().iloc[0]}")
print()


# =============================
# 4. Rating Distribution
# =============================
print("Rating Counts:")
print(df["rating"].value_counts().sort_index())
print()

# =============================
# 5. Price Distribution (Bins)
# =============================
print("Price Distribution (binned):")
print(pd.cut(df["price"], bins=5).value_counts().sort_index())
print()

# =============================
# 6. Notes for Interpretation
# =============================

# - Compare mean vs median for skewness
# - Check if ratings cluster at high values
# - Identify dominant price ranges
