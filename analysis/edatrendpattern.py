"""
Task 2 EDA –Trends, Patterns & Anomaly Detection
Project: Book Reviews Analysis
"""

import pandas as pd

# =============================
# 1. Load Cleaned Dataset
# =============================
df = pd.read_csv("data/eda-cleaned_books.csv")

print("Dataset loaded for trend analysis.\n")

# =============================
# 2. Correlation Analysis
# =============================
correlation = df["price"].corr(df["rating"])
print(f"Correlation between price and rating: {correlation:.3f}\n")

# =============================
# 3. Average Price by Rating
# =============================
avg_price_by_rating = df.groupby("rating")["price"].mean()
print("Average Price by Rating:")
print(avg_price_by_rating)
print()

# =============================
# 4. Identify Anomalies
# =============================
# Expensive but low-rated books
expensive_low_rated = df[(df["price"] > df["price"].quantile(0.75)) & (df["rating"] <= 2)]

# Cheap but highly rated books
cheap_high_rated = df[(df["price"] < df["price"].quantile(0.25)) & (df["rating"] >= 4)]

print(f"Expensive & Low-Rated Books: {len(expensive_low_rated)}")
print(f"Cheap & High-Rated Books: {len(cheap_high_rated)}\n")

# =============================
# 5. Preview Anomalies
# =============================
print("Sample Expensive & Low-Rated Books:")
print(expensive_low_rated.head())

print("\nSample Cheap & High-Rated Books:")
print(cheap_high_rated.head())
