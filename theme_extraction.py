import pandas as pd
from collections import Counter
import re

# Load sentiment results
df = pd.read_csv('sentiment_results.csv')

# Function to clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

# Common words to ignore
stop_words = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 
              'on', 'at', 'to', 'for', 'of', 'is', 'it',
              'this', 'that', 'was', 'are', 'with', 'have',
              'be', 'as', 'by', 'not', 'so', 'my', 'i',
              'they', 'we', 'you', 'he', 'she', 'its']

# Get all words from reviews
all_words = []
for text in df['Text']:
    words = clean_text(text).split()
    words = [w for w in words if w not in stop_words and len(w) > 3]
    all_words.extend(words)

# Count top 10 words
top_words = Counter(all_words).most_common(10)

print("Top 10 themes in reviews:")
for word, count in top_words:
    print(f"  {word}: {count} times")