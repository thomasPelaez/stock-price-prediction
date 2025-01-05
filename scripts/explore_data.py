import pandas as pd
import matplotlib.pyplot as plt

# Define file paths as raw strings
file_path = r"C:\Users\thoma\OneDrive\Documents\stock-price-prediction\data\crude_oil_prices.csv"
processed_file_path = r"C:\Users\thoma\OneDrive\Documents\stock-price-prediction\data\processed_crude_oil_prices.csv"
visualization_path = r"C:\Users\thoma\OneDrive\Documents\stock-price-prediction\visualization\close_prices_with_moving_average.png"

# Ensure directories exist (manually create directories if needed)

# Load the dataset
try:
    data = pd.read_csv(file_path)
    print("Data successfully loaded!")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Preview the first few rows
print("\nFirst few rows of the dataset:")
print(data.head())

# Ensure 'Date' column is in datetime format
try:
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data = data.dropna(subset=['Date'])
    print("Date column successfully converted to datetime.")
except KeyError:
    print("Error: 'Date' column is missing.")
    exit()

# Sort data by date
data = data.sort_values(by='Date')

# Calculate a 7-day moving average
data['7-Day Moving Average'] = data['Close'].rolling(window=7).mean()

# Save processed data
try:
    data.to_csv(processed_file_path, index=False)
    print(f"Processed data saved to: {processed_file_path}")
except Exception as e:
    print(f"Error saving processed data: {e}")
    exit()

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], label="Close Prices", color="blue")
plt.plot(data['Date'], data['7-Day Moving Average'], label="7-Day Moving Average", color="red")
plt.title("Crude Oil Close Prices with 7-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

# Save the plot
try:
    plt.savefig(visualization_path, dpi=300)
    print(f"Plot saved to: {visualization_path}")
except Exception as e:
    print(f"Error saving plot: {e}")
plt.show()
plt.close()