import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# File path to the enhanced dataset
file_path = "C:\\Users\\thoma\\OneDrive\\Documents\\stock-price-prediction\\data\\enhanced_crude_oil_prices.csv"

try:
    # Load the enhanced dataset
    data = pd.read_csv(file_path)
    print("Enhanced dataset successfully loaded!")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Display basic information about the dataset
print("\nDataset Info:")
print(data.info())

print("\nFirst 5 rows of the dataset:")
print(data.head())

# Generate summary statistics for numeric columns
print("\nSummary Statistics:")
print(data.describe())

# Exclude non-numeric columns for the correlation matrix
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Plot the heatmap for the correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_data.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix for Numeric Features")
plt.show()

# Save the correlation matrix heatmap
output_image_path = "C:\\Users\\thoma\\OneDrive\\Documents\\stock-price-prediction\\visualizations\\correlation_matrix.png"
plt.savefig(output_image_path, dpi=300)
print(f"\nCorrelation matrix heatmap saved to: {output_image_path}")