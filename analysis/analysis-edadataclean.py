"""
Task 2 EDA – Data Cleaning
Project: Book Reviews Analysis
"""

import pandas as pd

# =============================
# 1. Load Dataset
# =============================
df = pd.read_csv("data/raw_books.csv")

print("Initial dataset shape:", df.shape)

# =============================
# 2. Clean Price Column
# =============================
# Remove currency symbols and encoding issues
df["price"] = (
    df["price"]
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .astype(float)
)

print("Price column cleaned.")

# =============================
# 3. Clean Rating Column
# =============================
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating"] = df["rating"].map(rating_map)

print("Rating column converted to numeric.")

# =============================
# 4. Drop Unnecessary Columns
# =============================
df.drop(columns=["availability"], inplace=True)

print("Availability column dropped.")

# =============================
# 5. Check for Duplicates
# =============================
duplicates = df.duplicated().sum()
print(f"Duplicate rows: {duplicates}")

# =============================
# 6. Outlier Detection (IQR Method)
# =============================
Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["price"] < lower_bound) | (df["price"] > upper_bound)]

print(f"Outliers detected in price: {len(outliers)}")

# =============================
# 7. Save Cleaned Dataset
# =============================
df.to_csv("data/eda-cleaned_books.csv", index=False)

print("Cleaned dataset saved as data/eda-cleaned_books.csv")
print("Final dataset shape:", df.shape)
