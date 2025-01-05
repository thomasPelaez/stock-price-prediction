import pandas as pd
import matplotlib.pyplot as plt

# Define the file path
file_path = r"C:\Users\thoma\OneDrive\Documents\stock-price-prediction\data\crude_oil_prices.csv"

# Step 1: Load the dataset
try:
    # Load data, skipping the first row with headers
    data = pd.read_csv(file_path)
    print(f"File path being used: {file_path}")
    print("Data successfully loaded!")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Step 2: Print the first few rows to confirm correct parsing
print("\nFirst few rows of the dataset:")
print(data.head())

# Step 3: Calculate summary statistics
print("\nSummary Statistics for Close Prices:")
print(data["Close"].describe())

# Step 4: Calculate the 7-Day Moving Average
data["7-Day Moving Average"] = data["Close"].rolling(window=7).mean()

# Step 5: Handle missing data
data.dropna(subset=["Close", "7-Day Moving Average"], inplace=True)

# Step 6: Plotting the data
plt.figure(figsize=(14, 8))  # Increase figure size

# Plot Close Prices
plt.plot(data["Date"], data["Close"], label="Close Prices", color="blue", linewidth=1)

# Plot 7-Day Moving Average
plt.plot(data["Date"], data["7-Day Moving Average"], label="7-Day Moving Average", color="red", linewidth=2)

# Customize the X-axis
plt.xticks(rotation=45)  # Rotate the x-axis labels
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))  # Show fewer date labels

# Add Grid, Title, and Labels
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("Crude Oil Close Prices with 7-Day Moving Average", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Price", fontsize=14)

# Add Legend
plt.legend(fontsize=12)

# Improve Layout
plt.tight_layout()

# Show the Plot
plt.show()