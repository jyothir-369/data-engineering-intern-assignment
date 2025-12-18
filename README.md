# Data Engineering Intern Assignment - Monthly Stock Data Aggregation

## Overview

This project transforms a 2-year daily stock price dataset for 10 major tickers into monthly aggregated records. It accurately computes OHLC values for each month and derives key technical indicators (SMA 10, SMA 20, EMA 10, EMA 20) using only Pandas, without relying on any third-party technical analysis libraries.

The result is a clean, partitioned output: one well-structured CSV file per ticker containing exactly 24 monthly records.

## Project Structure
data-engineering-intern-assignment/
├── data/
│   └── stock_data.csv                  # Input dataset (place here)
├── src/
│   ├── init.py
│   └── process_data.py                 # Core processing logic
├── output/                             # Generated results
│   └── result_<TICKER>.csv             # e.g., result_AAPL.csv
├── README.md                           # Project documentation
├── requirements.txt
└── .gitignore
text## Input Data

- **File**: `data/stock_data.csv`
- **Columns**: `date, volume, open, high, low, close, adjclose, ticker`
- **Tickers**: `AAPL, AMD, AMZN, AVGO, CSCO, MSFT, NFLX, PEP, TMUS, TSLA`
- **Frequency**: Daily
- **Coverage**: 2 full years → 24 complete months

## Processing Logic

### Monthly Aggregation
Data is resampled to monthly frequency using precise rules:
- **Open** → Closing price of the first trading day of the month
- **Close** → Closing price of the last trading day of the month
- **High** → Maximum high price during the month
- **Low** → Minimum low price during the month

### Technical Indicators
All indicators are computed on monthly **close** prices post-aggregation:
- **SMA_10** & **SMA_20**: Simple Moving Average (rolling mean)
- **EMA_10** & **EMA_20**: Exponential Moving Average

**EMA Calculation** (standard formula):
- Smoothing factor (multiplier) = `2 / (period + 1)`
- `EMA_today = (Close_today × multiplier) + (EMA_yesterday × (1 - multiplier))`
- Initial EMA seeded from corresponding SMA for accuracy

Early rows contain `NaN` where insufficient history exists (expected behavior).

## Output

- **Directory**: `output/`
- **Files**: 10 CSVs → `result_AAPL.csv`, `result_MSFT.csv`, etc.
- **Rows per file**: Exactly 24 (one per month)
- **Columns**: `date, open, high, low, close, SMA_10, SMA_20, EMA_10, EMA_20`

## Key Assumptions

- Dataset has complete daily records with no missing months
- All provided dates are valid trading days (no need for filling gaps)
- Data is chronologically ordered within each ticker
- Uses raw `close` prices for indicator calculations (standard practice)

## Tech Stack

- **Language**: Python
- **Library**: Pandas (vectorized operations only)
- No external technical analysis libraries used

## How to Run

1. Place the dataset in `data/stock_data.csv`
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

Execute the script from the project root:Bashpython src/process_data.py
Monthly result files will be generated in the output/ directory

Author
Jyothir Raghavalu Bhogi
LinkedIn Profile
