import pandas as pd

# Define file paths
processed_file_path = r"C:\Users\thoma\OneDrive\Documents\stock-price-prediction\data\processed_crude_oil_prices.csv"
enhanced_file_path = r"C:\Users\thoma\OneDrive\Documents\stock-price-prediction\data\enhanced_crude_oil_prices.csv"

# Load the processed dataset
try:
    data = pd.read_csv(processed_file_path)
    print("Processed data successfully loaded!")
except FileNotFoundError:
    print(f"File not found: {processed_file_path}")
    exit()

# Feature 1: Daily Price Change
data['Daily Price Change'] = data['Close'] - data['Open']

# Feature 2: Volatility
data['Volatility'] = data['High'] - data['Low']

# Feature 3: Percentage Change
data['Percentage Change'] = data['Close'].pct_change() * 100

# Feature 4: Additional Moving Averages
data['14-Day Moving Average'] = data['Close'].rolling(window=14).mean()
data['30-Day Moving Average'] = data['Close'].rolling(window=30).mean()

# Feature 5: Lag Features
data['Close(t-1)'] = data['Close'].shift(1)
data['Close(t-2)'] = data['Close'].shift(2)

# Drop rows with NaN values caused by rolling and shifting
data = data.dropna()

# Save the enhanced dataset
try:
    data.to_csv(enhanced_file_path, index=False)
    print(f"Enhanced dataset saved to: {enhanced_file_path}")
except Exception as e:
    print(f"Error saving enhanced dataset: {e}")
