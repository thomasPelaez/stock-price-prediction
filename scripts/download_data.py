import yfinance as yf
import os

def download_stock_data(ticker, start_date, end_date, output_path):
    """
    Download financial data for a given ticker and save it aas a CSV file.

    Parameters:
        ticker (str): Ticker symbol ("CL=F" as we will be analyzing Cruse Oil Futures)
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
        output_path (str): Path to save the CSV file.
    """
    print(f"Downloading data for {ticker} from {start_date} to {end_date}") 

    # Download data using yfinance
    data = yf.download(ticker, start=start_date, end=end_date)

    # Create the output directory if it does not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the data to a CSV file
    data.to_csv(output_path)
    print(f"Data saved to {output_path}")

if __name__ =="__main__":
    # Example usage: Download Crude Oil Futures data
    ticker = "CL=F"
    start_date = "2020-01-01"
    end_date = "2023-12-31"
    output_path = "C:/Users/thoma/OneDrive/Documents/stock-price-prediction/data/crude_oil_prices.csv"

    # Call the function
    download_stock_data(ticker, start_date, end_date, output_path)