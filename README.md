Data Engineering Intern Assignment – Monthly Stock Data Aggregation
Overview
This project transforms a 2-year daily stock price dataset for 10 major stock tickers into monthly aggregated records. It accurately computes OHLC (Open, High, Low, Close) values per month and derives key technical indicators using only Pandas, without relying on any third-party technical analysis libraries.
The final output is a clean, partitioned dataset:

One CSV file per ticker
Exactly 24 monthly records per file

Project Structure

data-engineering-intern-assignment/
├── data/
│   └── stock_data.csv          # Input dataset
├── src/
│   ├── __init__.py
│   └── process_data.py         # Core data processing logic
├── output/
│   └── result_.csv             # e.g., result_AAPL.csv
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies
└── .gitignore

Input Data

File: data/stock_data.csv
Columns: date, volume, open, high, low, close, adjclose, ticker
Tickers: AAPL, AMD, AMZN, AVGO, CSCO, MSFT, NFLX, PEP, TMUS, TSLA
Frequency: Daily
Coverage: 2 full years → 24 complete months

Processing Logic
Monthly Aggregation
Daily stock data is resampled to monthly frequency using the following rules:

Open → Price from the first trading day of the month
Close → Price from the last trading day of the month
High → Maximum high price during the month
Low → Minimum low price during the month
Volume → Monthly total (sum)

Technical Indicators
All indicators are computed on monthly close prices after aggregation:

SMA_10 – 10-period Simple Moving Average
SMA_20 – 20-period Simple Moving Average
EMA_10 – 10-period Exponential Moving Average
EMA_20 – 20-period Exponential Moving Average

EMA Calculation Formula

Multiplier: 2 / (period + 1)
Formula:
EMA_today = (Close_today × multiplier) + (EMA_yesterday × (1 − multiplier))

Initial EMA values are seeded using the corresponding SMA for numerical stability.
Early rows will contain NaN values where insufficient historical data exists — this is expected behavior.
Output

Directory: output/
Files Generated:
result_AAPL.csv, result_AMD.csv, result_AMZN.csv, ...
Rows per file: Exactly 24 rows (one per month)
Output Columns: date, open, high, low, close, SMA_10, SMA_20, EMA_10, EMA_20

Key Assumptions

Dataset contains complete daily records with no missing months
All dates correspond to valid trading days
Data is chronologically ordered per ticker
Indicators are calculated using raw close prices (standard market practice)

Tech Stack

Programming Language: Python
Primary Library: Pandas
Processing Style: Vectorized operations
❌ No external technical analysis libraries used

How to Run

Place the dataset in: data/stock_data.csv
Install required dependencies:Bashpip install -r requirements.txt
Execute the script from the project root:Bashpython src/process_data.py
Generated monthly CSV files will appear in: output/


Author: Jyothir Raghavalu Bhogi
🔗 LinkedIn Profile
