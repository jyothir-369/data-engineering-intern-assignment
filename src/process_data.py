import pandas as pd
import os


def fetch_data(file_location: str) -> pd.DataFrame:
    dataframe = pd.read_csv(file_location, parse_dates=["date"])
    dataframe = dataframe.sort_values(["ticker", "date"])
    return dataframe


def summarize_and_compute(dataframe: pd.DataFrame) -> pd.DataFrame:
    result = []

    for ticker, ticker_dataframe in dataframe.groupby("ticker"):
        ticker_dataframe = ticker_dataframe.set_index("date")

        monthly = (
            ticker_dataframe
            .resample("ME") 
            .agg(
                opening_price=("open", "first"),
                highest_price=("high", "max"),
                lowest_price=("low", "min"),
                closest_price=("close", "last"),
                trade_volume=("volume", "sum"),
                adjusted_price=("adjclose", "last"),
            )
            .reset_index()
        )

        monthly["simple_ma_10"] = monthly["closest_price"].rolling(10).mean()
        monthly["simple_ma_20"] = monthly["closest_price"].rolling(20).mean()

        monthly["exp_ma_10"] = monthly["closest_price"].ewm(span=10, adjust=False).mean()
        monthly["exp_ma_20"] = monthly["closest_price"].ewm(span=20, adjust=False).mean()

        monthly["ticker"] = ticker
        result.append(monthly)

    return pd.concat(result, ignore_index=True)


def save_results(dataframe: pd.DataFrame, output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)

    for ticker, ticker_dataframe in dataframe.groupby("ticker"):
        output_path = os.path.join(output_dir, f"result_{ticker}.csv")
        ticker_dataframe.to_csv(output_path, index=False)


def execute():
    source_file = "data/stock_data.csv"
    destination_dir = "output"

    raw_data = fetch_data(source_file)
    final_data = summarize_and_compute(raw_data)

    save_results(final_data, destination_dir)


if __name__ == "__main__":
    execute()