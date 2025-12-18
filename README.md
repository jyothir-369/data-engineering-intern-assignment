# 📊 Data Engineering Intern Assignment

## Monthly Stock Data Aggregation & Technical Indicator Pipeline

---

## 🚀 Project Overview

This project demonstrates a **production-quality data engineering pipeline** that converts **2 years of daily stock market data** into **clean, analytics-ready monthly datasets**.

Using **pure Pandas (no TA libraries)**, the pipeline:

* Aggregates daily OHLCV data into **monthly OHLC records**
* Computes widely used **technical indicators**
* Outputs **partitioned, standardized CSV files** ready for downstream analytics or ML workflows

### ✅ Final Deliverables

* **One CSV per ticker**
* **Exactly 24 monthly records per file**
* **Consistent schema across all outputs**

---

## 🧠 Key Highlights

* 📈 Accurate **OHLC aggregation logic**
* 🧮 Manual implementation of **SMA & EMA indicators**
* ⚡ Efficient, vectorized Pandas operations
* 📁 Clean, partitioned output design (industry best practice)
* 🚫 Zero reliance on third-party technical analysis libraries

---

## 📂 Project Structure

```
data-engineering-intern-assignment/
├── data/
│   └── stock_data.csv          # Raw daily stock price data
├── src/
│   ├── __init__.py
│   └── process_data.py         # Core data transformation pipeline
├── output/
│   └── result_<TICKER>.csv     # e.g., result_AAPL.csv
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── .gitignore
```

---

## 📥 Input Dataset

**Location:** `data/stock_data.csv`

### Dataset Schema

| Column   | Description              |
| -------- | ------------------------ |
| date     | Trading date             |
| open     | Opening price            |
| high     | Highest price of the day |
| low      | Lowest price of the day  |
| close    | Closing price            |
| adjclose | Adjusted closing price   |
| volume   | Daily trading volume     |
| ticker   | Stock ticker symbol      |

### Supported Tickers

```
AAPL, AMD, AMZN, AVGO, CSCO, MSFT, NFLX, PEP, TMUS, TSLA
```

* **Frequency:** Daily
* **Coverage:** 2 full years
* **Expected Output:** 24 complete months per ticker

---

## ⚙️ Data Processing Logic

### 📆 Monthly OHLC Aggregation

Daily stock records are resampled into **monthly intervals** using industry-standard financial rules:

| Field  | Aggregation Strategy           |
| ------ | ------------------------------ |
| Open   | First trading day of the month |
| Close  | Last trading day of the month  |
| High   | Maximum price during the month |
| Low    | Minimum price during the month |
| Volume | Sum of daily volumes           |

---

## 📐 Technical Indicator Computation

All indicators are calculated **after monthly aggregation**, using **monthly closing prices**.

### Indicators Implemented

* **SMA_10** – 10-period Simple Moving Average
* **SMA_20** – 20-period Simple Moving Average
* **EMA_10** – 10-period Exponential Moving Average
* **EMA_20** – 20-period Exponential Moving Average

---

### 🔢 EMA Formula (Manually Implemented)

**Multiplier**

```
2 / (period + 1)
```

**EMA Calculation**

```
EMA_today = (Close_today × multiplier)
          + (EMA_yesterday × (1 − multiplier))
```

📌 Initial EMA values are **seeded using SMA values** to ensure numerical stability.
📉 Early periods naturally contain `NaN` values due to insufficient historical data.

---

## 📤 Output Specification

**Directory:** `output/`

**Generated Files**

```
result_AAPL.csv
result_AMD.csv
result_AMZN.csv
...
```

### Output Schema

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

* 📅 One row per month
* 📊 Exactly **24 rows per ticker**
* 🧹 Clean, analysis-ready format

---

## 🧩 Design Assumptions

* Complete daily trading data with **no missing months**
* All dates correspond to **valid market trading days**
* Data is **chronologically ordered per ticker**
* Indicators are calculated using **raw close prices** (standard market convention)

---

## 🛠️ Technology Stack

* **Language:** Python
* **Core Library:** Pandas
* **Computation Style:** Vectorized operations

❌ **No external technical analysis libraries** (e.g., TA-Lib, pandas-ta)

---

## ▶️ How to Run the Pipeline

1. Place the input file at:

   ```
   data/stock_data.csv
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute the pipeline:

   ```bash
   python src/process_data.py
   ```

📁 Monthly aggregated CSV files will be generated in the `output/` directory.

---

## 👨‍💻 Author

**Jyothir Raghavalu Bhogi**
📌 Data Engineering & Analytics
🔗 [LinkedIn](https://www.linkedin.com/)

---

⭐ *This project is designed to reflect real-world data engineering standards and financial data processing best practices.*
