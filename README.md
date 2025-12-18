# Data Engineering Intern Assignment – Monthly Stock Data Aggregation

## Overview

This project transforms a **2-year daily stock price dataset** for **10 major stock tickers** into **monthly aggregated records**. It accurately computes **OHLC (Open, High, Low, Close)** values per month and derives key **technical indicators** using **only Pandas**, without relying on any third-party technical analysis libraries.

### Final Output

* One CSV file per ticker
* Exactly **24 monthly records** per file

---

## Project Structure

```
data-engineering-intern-assignment/
├── data/
│   └── stock_data.csv          # Input dataset
├── src/
│   ├── __init__.py
│   └── process_data.py         # Core data processing logic
├── output/
│   └── result_<TICKER>.csv     # e.g., result_AAPL.csv
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies
└── .gitignore
```

---

## Input Data

**File:** `data/stock_data.csv`

**Columns:**

* `date`
* `volume`
* `open`
* `high`
* `low`
* `close`
* `adjclose`
* `ticker`

**Tickers:**

```
AAPL, AMD, AMZN, AVGO, CSCO, MSFT, NFLX, PEP, TMUS, TSLA
```

**Frequency:** Daily
**Coverage:** 2 full years → **24 complete months**

---

## Processing Logic

### Monthly Aggregation

Daily stock data is resampled to **monthly frequency** using the following rules:

| Field  | Aggregation Rule                                  |
| ------ | ------------------------------------------------- |
| Open   | Price from the **first trading day** of the month |
| Close  | Price from the **last trading day** of the month  |
| High   | **Maximum** high price during the month           |
| Low    | **Minimum** low price during the month            |
| Volume | **Sum** of daily volumes (monthly total)          |

---

## Technical Indicators

All indicators are computed **after monthly aggregation**, using **monthly close prices**.

### Indicators Calculated

* **SMA_10**: 10-period Simple Moving Average
* **SMA_20**: 20-period Simple Moving Average
* **EMA_10**: 10-period Exponential Moving Average
* **EMA_20**: 20-period Exponential Moving Average

---

### EMA Calculation Formula

**Multiplier:**

```
2 / (period + 1)
```

**Formula:**

```
EMA_today = (Close_today × multiplier) + (EMA_yesterday × (1 - multiplier))
```

Initial EMA values are seeded using the corresponding **SMA** for numerical stability.

> ⚠️ Early rows will contain `NaN` values where insufficient historical data exists — this is expected behavior.

---

## Output

**Directory:** `output/`

**Files Generated:**

```
result_AAPL.csv
result_AMD.csv
result_AMZN.csv
...
```

**Rows per File:** Exactly **24 rows** (one per month)

### Output Columns

| Column |
| ------ |
| date   |
| open   |
| high   |
| low    |
| close  |
| SMA_10 |
| SMA_20 |
| EMA_10 |
| EMA_20 |

---

## Key Assumptions

* Dataset contains **complete daily records** with no missing months
* All dates correspond to **valid trading days**
* Data is **chronologically ordered per ticker**
* Indicators are calculated using **raw close prices** (standard market practice)

---

## Tech Stack

* **Programming Language:** Python
* **Primary Library:** Pandas
* **Processing Style:** Vectorized operations

❌ **No external technical analysis libraries** (e.g., TA-Lib) are used or allowed.

---

## How to Run

1. Place the input dataset at:

   ```
   data/stock_data.csv
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the processing script from the project root:

   ```bash
   python src/process_data.py
   ```

📁 Monthly CSV files will be generated in the `output/` directory.

---

## Author

**Jyothir Raghavalu Bhogi**
🔗 [LinkedIn Profile](https://www.linkedin.com/)
