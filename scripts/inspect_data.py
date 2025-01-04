import pandas as pd 

# Define the file path
file_path = "C:/Users/thoma/OneDrive/Documents/stock-price-prediction/data/stock_prices.csv"

# Load the data
data = pd.read_csv(file_path, skiprows=2)

# Display first 5 rows
print("Frist 5 rows of the dataset:")
print(data.head())

# Display dataset info
print("\nDataset Info::")
print(data.info())

# Display sumary statistics
print("\nSummary Statistics:")
print(data.describe())

# Drop rows with missing values
data = data.dropna()

# Convert the 'Date' column to datetime and sort by datea
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values(by='Date')

# Save the cleaned data
cleaned_file_path = "C:/Users/thoma/OneDrive/Documents/stock-price-prediction/data/clean_stock_prices.csv"
data.to_csv(cleaned_file_path, index=False)

print("\nData cleaned and saved!")