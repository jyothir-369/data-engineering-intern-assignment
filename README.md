# Data Engineering Intern Assignment - Monthly Stock Data Aggregation

## Overview

This project processes a 2-year daily stock price dataset containing 10 tickers and transforms it into monthly aggregated data. For each ticker, it computes OHLC values for each month and calculates technical indicators (SMA 10, SMA 20, EMA 10, EMA 20) based on the monthly closing prices. The output consists of one CSV file per ticker.

## Project Structure
data-engineering-intern-assignment/
├── data/
│   └── stock_data.csv                  # Input dataset (to be placed here)
├── src/
│   ├── init.py
│   └── process_data.py                 # Main processing script
├── output/                             # Generated output files
│   └── result_<TICKER>.csv             # One file per ticker (e.g., result_AAPL.csv)
├── README.md                           # This file
├── requirements.txt
└── .gitignore
text## Input Data

- File: `data/stock_data.csv`
- Columns: `date, volume, open, high, low, close, adjclose, ticker`
- Tickers: `AAPL, AMD, AMZN, AVGO, CSCO, MSFT, NFLX, PEP, TMUS, TSLA`
- Frequency: Daily
- Period: 2 years (24 complete months)

## Processing Logic

### Monthly Aggregation
Data is resampled to monthly frequency with the following rules:
- **Open**: Price on the first trading day of the month
- **Close**: Price on the last trading day of the month
- **High**: Maximum high price during the month
- **Low**: Minimum low price during the month

### Technical Indicators
Calculated on the monthly `close` prices after aggregation:
- **SMA_10**: Simple Moving Average over 10 months
- **SMA_20**: Simple Moving Average over 20 months
- **EMA_10**: Exponential Moving Average over 10 months
- **EMA_20**: Exponential Moving Average over 20 months

EMA is calculated using the standard formula:
- Multiplier = 2 / (period + 1)
- EMA_today = (Close_today × Multiplier) + (EMA_yesterday × (1 - Multiplier))
- Initial EMA value seeded with the corresponding SMA

Values are `NaN` where insufficient prior data exists (e.g., first 9 rows for SMA_10/EMA_10).

## Output

- Location: `output/` directory
- Files: 10 CSV files named `result_<TICKER>.csv` (e.g., `result_AAPL.csv`)
- Each file contains exactly 24 rows (one per month)
- Columns: `date, open, high, low, close, SMA_10, SMA_20, EMA_10, EMA_20`

## Assumptions

- The input dataset contains complete daily trading data with no missing months over the 2-year period.
- All dates are trading days (no gaps requiring forward/backward fill).
- The `date` column is in a parseable format and sorted chronologically within each ticker.
- Adjusted close (`adjclose`) is present but not used in calculations (standard close is used as per common practice for indicators).

## Tech Stack

- Python
- Pandas (only standard Pandas operations; no third-party technical analysis libraries)

## How to Run

1. Place the provided dataset as `data/stock_data.csv`
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

Run the script from the project root:Bashpython src/process_data.py
Output files will be generated in the output/ directory.

Author
Jyothir Raghavalu Bhogi