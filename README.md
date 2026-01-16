# Book Review Data Analysis Project

This project analyzes book data scraped from an online bookstore to uncover insights about pricing, ratings, and patterns in reader satisfaction. The project follows a structured data analysis workflow from web scraping to exploratory data analysis and visualization.

## Project Structure

book_reviews_project/
├── analysis/        # Analysis scripts (EDA, statistics, trends)
├── data/            # Raw and cleaned datasets
├── charts/          # Visualizations (Task 3)
├── scraper/         # Web scraping scripts
├── notebooks/       # Optional Jupyter notebooks
├── README.md
├── requirements.txt
└── .gitignore

## Project Tasks

### Task 1: Web Scraping
- Scraped book data including title, price, rating, and availability
- Saved raw data into CSV format
- Performed initial inspection and preprocessing

### Task 2: Exploratory Data Analysis (EDA)
- Cleaned and prepared scraped data
- Converted prices and ratings into numeric formats
- Performed statistical analysis (mean, median, mode, distributions)
- Analyzed trends, patterns, and anomalies
- Identified value-for-money and overpriced books
- Documented findings in a detailed EDA report

### Task 3: Data Visualization (Upcoming)
- Visualize price and rating distributions
- Explore relationships between variables
- Highlight anomalies using charts

### Task 4: Sentiment Analysis (Planned)
- Apply sentiment analysis to book reviews
- Compare sentiment scores with numeric ratings

## Key Insights (EDA)

- Book prices are not strongly correlated with ratings
- Highly rated books tend to be more affordable
- Several expensive books received low ratings
- The dataset is balanced and suitable for further analysis

## Tools & Technologies

- Python
- Pandas
- NumPy
- BeautifulSoup
- Matplotlib / Seaborn (Task 3)
- Git & GitHub
