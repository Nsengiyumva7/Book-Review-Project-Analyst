# ----------------------------------------
#  Task 1 Final Mini-project: Web scraping analysis Visualization & Sentiment Analysis
# ----------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ----------------------------------------
# Ensure charts folder exists
# ----------------------------------------
os.makedirs("charts", exist_ok=True)

# ----------------------------------------
# 1️⃣ Load Raw Data
# ----------------------------------------
df = pd.read_csv("data/raw_books.csv")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

# ----------------------------------------
# 2️⃣ Data Cleaning & Transformation
# ----------------------------------------

# ---- Clean 'price' column
# Remove all non-digit/non-dot characters (removes £, Â, etc.)
df["price"] = df["price"].str.replace(r"[^\d.]", "", regex=True).astype(float)

# ---- Convert rating text → numeric
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["rating_numeric"] = df["rating"].map(rating_map)

# ---- Clean availability column
# Extract only numbers from text
df["availability"] = df["availability"].str.replace(r"\D+", "", regex=True)
# Convert empty strings to 0, then to integer
df["availability"] = df["availability"].replace("", "0").astype(int)

print("\nCleaned data sample:")
print(df.head())

# ----------------------------------------
# 3️⃣ Exploratory Data Analysis (EDA)
# ----------------------------------------

# Rating distribution
print("\nRating distribution:")
print(df["rating_numeric"].value_counts().sort_index())

# Price statistics
print("\nPrice statistics:")
print(df["price"].describe())

# Availability statistics
print("\nAvailability statistics:")
print(df["availability"].describe())

# ----------------------------------------
# 4️⃣ Data Visualization
# ----------------------------------------

# ---- Rating distribution
plt.figure(figsize=(8, 5))
sns.countplot(x="rating_numeric", data=df, palette="viridis")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/rating_distribution.png", dpi=300)
plt.show()

# ---- Price vs Rating
plt.figure(figsize=(8, 5))
sns.boxplot(x="rating_numeric", y="price", data=df, palette="magma")
plt.title("Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.savefig("charts/price_vs_rating.png", dpi=300)
plt.show()

# ---- Availability histogram
plt.figure(figsize=(8, 5))
sns.histplot(df["availability"], bins=10, color="skyblue")
plt.title("Availability Distribution")
plt.xlabel("Number of books in stock")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/availability_distribution.png", dpi=300)
plt.show()

# ----------------------------------------
# 5️⃣ Sentiment Analysis (Rule-Based)
# ----------------------------------------
# Using rating as sentiment proxy
def sentiment_label(rating):
    if rating >= 4:
        return "Positive"
    elif rating == 3:
        return "Neutral"
    else:
        return "Negative"

df["sentiment"] = df["rating_numeric"].apply(sentiment_label)

print("\nSentiment distribution:")
print(df["sentiment"].value_counts())

# ----------------------------------------
# 6️⃣ Save Final Datasets
# ----------------------------------------

# Save numeric cleaned dataset BEFORE adding sentiment
df.drop(columns=["sentiment"], errors="ignore").to_csv(
    "data/cleaned_books.csv", index=False, encoding="utf-8"
)

# Then add sentiment and save the other file
# save new /
df["sentiment"] = df["rating_numeric"].apply(sentiment_label)
df.to_csv("data/books_with_sentiment.csv", index=False, encoding="utf-8")


print("\nSaved files:")
print("- data/cleaned_books.csv")
print("- data/books_with_sentiment.csv")

print("\n🎉 Task 1 (Web Scraping) Final Mini-project Finished!")
print("\nProject Finished!")
