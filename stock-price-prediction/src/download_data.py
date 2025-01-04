import yfinance as yf
import pandas as pd

# Defines stock ticker and date range
ticker = 'AAPL' # Apple inc
start_date = '2020-01-01'
end_date = '2023-01-01'

# Download of the data
print(f"Downloading data for {ticker} from {start_date} to {end_date}")
stock_data = yf.download(ticker, start=start_date, end=end_date, interval="1d")

# Save data to CSV file
output_path = "C:/Users/thoma/OneDrive/Documents/stock-price-prediction/data/stock_prices.csv"
stock_data.to_csv(output_path, index=True)

print(f"Data downloaded and saved to {output_path}")