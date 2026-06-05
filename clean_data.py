import pandas as pd

# Load the dataset
df = pd.read_csv('Reviews.csv')

print("Before cleaning:", len(df))

# Keep only useful columns
df = df[['Score', 'Summary', 'Text']]

# Remove empty reviews
df = df.dropna()

# Remove duplicate reviews
df = df.drop_duplicates()

print("After cleaning:", len(df))

# Save cleaned data
df.to_csv('cleaned_reviews.csv', index=False)

print("Cleaned data saved!")