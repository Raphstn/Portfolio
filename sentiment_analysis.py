from textblob import TextBlob
import pandas as pd

# Function to classify the sentiment of a review
def classify_sentiment(text):
    """Classifies the sentiment of a given review as positive, neutral, or negative."""
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

# Function to apply sentiment analysis to the entire dataframe
def apply_sentiment_analysis(df):
    """Applies sentiment analysis to each review and adds a 'Sentiment' column."""
    df['Sentiment'] = df['Review_Text'].apply(classify_sentiment)
    return df

# Function to filter negative reviews
def filter_negative_reviews(df):
    """Filters the reviews that are classified as negative."""
    negative_reviews = df[df['Sentiment'] == 'negative']
    return negative_reviews

# Function to get the most criticized product categoris
def get_most_criticized_products(df, top_n=10):
    """Identifies the top N most criticized product categories."""
    negative_reviews = filter_negative_reviews(df)
    most_criticized_products = negative_reviews['Class_Name'].value_counts().head(top_n)
    return most_criticized_products
