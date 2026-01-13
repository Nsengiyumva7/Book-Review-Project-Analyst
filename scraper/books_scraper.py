# ----------------------------------------
# Import required libraries
# ----------------------------------------
import requests
from bs4 import BeautifulSoup
import csv
import time


# ----------------------------------------
# Base URL for pagination
# ----------------------------------------
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"


# ----------------------------------------
# Headers to mimic a real browser
# (Helps avoid being blocked)
# ----------------------------------------
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}


# ----------------------------------------
# Container to store scraped data
# ----------------------------------------
books_data = []


# ----------------------------------------
# Loop through pages (pagination)
# ----------------------------------------
for page in range(1, 6):

    print(f"\nScraping page {page}...")

    # Construct the page URL
    url = BASE_URL.format(page)

    try:
        # ----------------------------------------
        # Send HTTP request with headers & timeout
        # ----------------------------------------
        response = requests.get(url, headers=HEADERS, timeout=10)

        # ----------------------------------------
        # Check HTTP status
        # ----------------------------------------
        if response.status_code != 200:
            print(f"⚠️ Failed page {page} (Status {response.status_code})")
            continue

        # ----------------------------------------
        # Parse HTML using BeautifulSoup
        # ----------------------------------------
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all book containers on the page
        books = soup.find_all("article", class_="product_pod")

        # If no books found, stop scraping
        if not books:
            print("⚠️ No books found. Stopping pagination.")
            break

        # ----------------------------------------
        # Extract data from each book
        # ----------------------------------------
        for book in books:
            try:
                # Book title
                title = book.h3.a.get("title", "").strip()

                # Book price
                price = book.find("p", class_="price_color").text.strip()

                # Availability text
                availability = book.find(
                    "p", class_="instock availability"
                ).text.strip()

                # Rating (One, Two, Three, etc.)
                rating = book.p["class"][1]

                # Append data as a row
                books_data.append([
                    title,
                    price,
                    rating,
                    availability
                ])

            except Exception as e:
                # Catch parsing errors for individual books
                print(f"⚠️ Error parsing a book: {e}")
                continue

        # ----------------------------------------
        # Polite delay between requests
        # ----------------------------------------
        time.sleep(1)

    except requests.exceptions.RequestException as e:
        # Catch network-related errors
        print(f"❌ Request failed on page {page}: {e}")
        continue


# ----------------------------------------
# Save scraped data to CSV file
# ----------------------------------------
with open("data/raw_books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow([
        "title",
        "price",
        "rating",
        "availability"
    ])

    # Write data rows
    writer.writerows(books_data)


# ----------------------------------------
# Final success message
# ----------------------------------------
print(f"\n✅ Saved {len(books_data)} books to data/raw_books.csv")
