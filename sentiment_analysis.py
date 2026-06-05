import pandas as pd
from textblob import TextBlob

# Load cleaned data
df = pd.read_csv('cleaned_reviews.csv')

df = df.head(1000)

# Function to get sentiment
def get_sentiment(text):
    analysis = TextBlob(str(text))
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Apply sentiment to each review
df['Sentiment'] = df['Text'].apply(get_sentiment)

# Show results
print(df['Sentiment'].value_counts())

# Save results
df.to_csv('sentiment_results.csv', index=False)
print("Sentiment analysis done!")