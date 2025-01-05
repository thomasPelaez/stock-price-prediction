import pandas as pd 

# Define the file path
file_path = "C:/Users/thoma/OneDrive/Documents/stock-price-prediction/data/crude_oil_prices.csv"

# Load the data
try:
    data=pd.read_csv(file_path)
    print("Data succesfully loaded")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Drop unnecessary rows (for example index 0 and 1 inf htey contain invalid data)
data.dropna(inplace=True)

# Convert numeric columns to appropriate data types
numeric_columns = ["Open", "High", "Low", "Close", "Volume"]
for col in numeric_columns:
    data[col] = pd.to_numeric(data[col], errors="coerce") #Handles invalid conversions

# Inspect the first few rows of data
print("\nFirst 5 rows of hte dataset:")
print(data.head())

# Check for missing values
print("\nMissing values in the dataset:")
print(data.isnull().sum())

# Display the dataset's overall structure
print("\nDataset Info:")
print(data.info)