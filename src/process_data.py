import pandas as pandas
import os

def load_stock_data(file_path):
    stock_data = pandas.read_csv(file_path, parse_dates=["date"])
    stock_data = stock_data.sort_values(["ticker", "date"])
    return stock_data

def get_monthly_data(stock_data):
    all_tickers = []

    for ticker, data_for_one_ticker in stock_data.groupby("ticker"):
        data_for_one_ticker = data_for_one_ticker.set_index("date")

        monthly = data_for_one_ticker.resample("ME").agg(
            open=("open", "first"),
            high=("high", "max"),
            low=("low", "min"),
            close=("close", "last"),
            volume=("volume", "sum")
        )

        monthly["SMA_10"] = monthly["close"].rolling(10).mean()
        monthly["SMA_20"] = monthly["close"].rolling(20).mean()

        def calculate_ema(prices, period, sma_values):
            ema_list = []
            multiplier = 2 / (period + 1)
            for i in range(len(prices)):
                if i == 0:
                    first_value = prices.iloc[i] if pandas.isna(sma_values.iloc[i]) else sma_values.iloc[i]
                    ema_list.append(first_value)
                else:
                    ema_list.append((prices.iloc[i] * multiplier) + (ema_list[i - 1] * (1 - multiplier)))
            return pandas.Series(ema_list, index=prices.index)

        monthly["EMA_10"] = calculate_ema(monthly["close"], 10, monthly["SMA_10"])
        monthly["EMA_20"] = calculate_ema(monthly["close"], 20, monthly["SMA_20"])

        monthly["ticker"] = ticker
        monthly = monthly.reset_index()

       
        if len(monthly) > 24:
            monthly = monthly.tail(24)
        elif len(monthly) < 24:
           
            missing_rows = 24 - len(monthly)
            empty_rows = pandas.DataFrame(
                {
                    "date": [pandas.NaT]*missing_rows,
                    "open": [pandas.NA]*missing_rows,
                    "high": [pandas.NA]*missing_rows,
                    "low": [pandas.NA]*missing_rows,
                    "close": [pandas.NA]*missing_rows,
                    "volume": [pandas.NA]*missing_rows,
                    "SMA_10": [pandas.NA]*missing_rows,
                    "SMA_20": [pandas.NA]*missing_rows,
                    "EMA_10": [pandas.NA]*missing_rows,
                    "EMA_20": [pandas.NA]*missing_rows,
                    "ticker": [ticker]*missing_rows
                }
            )
            monthly = pandas.concat([empty_rows, monthly], ignore_index=True)

        all_tickers.append(monthly)

    combined_data = pandas.concat(all_tickers, ignore_index=True)
    return combined_data

def save_csv_files(monthly_data, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for ticker, data_for_one_ticker in monthly_data.groupby("ticker"):
        file_path = os.path.join(output_folder, f"result_{ticker}.csv")
        data_for_one_ticker.to_csv(file_path, index=False)

def run():
    input_file = "data/stock_data.csv"
    output_folder = "output"

    daily_stock_data = load_stock_data(input_file)
    monthly_stock_data = get_monthly_data(daily_stock_data)
    save_csv_files(monthly_stock_data, output_folder)

if __name__ == "__main__":
    run()
