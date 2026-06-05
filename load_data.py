import pandas as pd

# Load the dataset
df = pd.read_csv('Reviews.csv')

# Show basic information
print("Dataset loaded successfully!")
print("Total reviews:", len(df))
print("Columns:", df.columns.tolist())
print(df.head())