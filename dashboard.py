import streamlit as st
import pandas as pd
from collections import Counter
import re

st.title("🧠 AI Product Feedback Analyzer")
st.write("Analyzing Amazon customer reviews for Product Managers")

# Load data
df = pd.read_csv('sentiment_results.csv')

# Sentiment Chart
st.header("📊 Sentiment Analysis")
sentiment_counts = df['Sentiment'].value_counts()
st.bar_chart(sentiment_counts)

# Numbers
col1, col2, col3 = st.columns(3)
col1.metric("✅ Positive", sentiment_counts.get('Positive', 0))
col2.metric("😡 Negative", sentiment_counts.get('Negative', 0))
col3.metric("😐 Neutral", sentiment_counts.get('Neutral', 0))

# Top Themes
st.header("🔑 Top Themes")
stop_words = ['the','a','an','and','or','but','in','on',
              'at','to','for','of','is','it','this','that',
              'was','are','with','have','be','as','by','not',
              'so','my','i','they','we','you','he','she','its']

all_words = []
for text in df['Text']:
    words = re.sub(r'[^a-z\s]', '', str(text).lower()).split()
    words = [w for w in words if w not in stop_words and len(w) > 3]
    all_words.extend(words)

top_words = Counter(all_words).most_common(10)
words_df = pd.DataFrame(top_words, columns=['Word', 'Count'])
st.bar_chart(words_df.set_index('Word'))

# Sample Reviews
st.header("📝 Sample Reviews")
st.dataframe(df[['Summary', 'Sentiment']].head(10))