import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def plot_rating_distribution(df):
    """Plots the distribution of ratings."""
    plt.figure(figsize=(8,6))
    sns.histplot(df['Rating'], bins=5, kde=False, discrete=True)
    plt.title('Distribution of Ratings')
    plt.xlabel('Ratings')
    plt.ylabel('Number of Reviews')
    plt.show()

def plot_reviews_per_category(df):
    """Plots the number of reviews per product category."""
    plt.figure(figsize=(12,6))
    sns.countplot(data=df, x='Class_Name', order=df['Class_Name'].value_counts().index)
    plt.title('Number of Reviews by Product Category')
    plt.xticks(rotation=90)
    plt.show()

def plot_average_ratings_per_category(df):
    """Plots the average rating per product category."""
    plt.figure(figsize=(12,6))
    sns.barplot(x='Class_Name', y='Rating', data=df, estimator=np.mean)
    plt.title('Average Ratings by Product Category')
    plt.xticks(rotation=90)
    plt.show()


def plot_ratings_by_age_group(df):
    """Plots the distribution of ratings by age group with a customized median line."""
    # Create age groups
    df['Age_Group'] = pd.cut(df['Age'], bins=[18, 25, 35, 45, 55, 65, 100],
                             labels=['18-25', '26-35', '36-45', '46-55', '56-65', '65+'])

    # Plot the ratings distribution by age group
    plt.figure(figsize=(10, 6))

    # Only one sns.boxplot call with customized median line
    sns.boxplot(x='Age_Group', y='Rating', data=df, palette='coolwarm',
                medianprops={'color': 'black', 'linewidth': 2})  # Make the median line black and thicker

    plt.title('Distribution of Ratings by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Ratings')
    plt.show()

def plot_sentiment_distribution(df):
        """Plots the distribution of sentiments (positive, neutral, negative)."""
        # Count sentiment categories
        sentiment_counts = df['Sentiment'].value_counts()

        # Plot sentiment distribution
        plt.figure(figsize=(8, 6))
        sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='coolwarm')
        plt.title('Distribution of Review Sentiments')
        plt.xlabel('Sentiment')
        plt.ylabel('Number of Reviews')
        plt.show()

def plot_reviews_per_category(df):
    """Plots the number of reviews for each product category."""
    # Plot number of reviews by product category
    plt.figure(figsize=(12,6))
    sns.countplot(data=df, x='Class_Name', order=df['Class_Name'].value_counts().index, palette='coolwarm')
    plt.title('Number of Reviews per Product Category')
    plt.xticks(rotation=90)
    plt.xlabel('Product Category')
    plt.ylabel('Number of Reviews')
    plt.show()

def plot_avg_rating_per_category(df):
    """Plots the average rating for each product category."""
    # Plot average rating by product category
    plt.figure(figsize=(12,6))
    sns.barplot(x='Class_Name', y='Rating', data=df, estimator=np.mean, palette='coolwarm')
    plt.title('Average Rating per Product Category')
    plt.xticks(rotation=90)
    plt.xlabel('Product Category')
    plt.ylabel('Average Rating')
    plt.show()

def plot_category_popularity_by_age(df):
        """Plots the popularity of product categories based on age group."""
        # Plot number of reviews per product category by age group
        plt.figure(figsize=(12, 6))
        # Create age groups based on the 'Age' column
        df['Age_Group'] = pd.cut(df['Age'], bins=[18, 25, 35, 45, 55, 65, 100],
                                 labels=['18-25', '26-35', '36-45', '46-55', '56-65', '65+'])

        sns.countplot(data=df, x='Class_Name', hue='Age_Group', palette='coolwarm',
                      order=df['Class_Name'].value_counts().index)
        plt.title('Popularity of Product Categories by Age Group')
        plt.xticks(rotation=90)
        plt.xlabel('Product Category')
        plt.ylabel('Number of Reviews')
        plt.legend(title='Age Group')
        plt.show()


import pandas as pd
import matplotlib.pyplot as plt


def analyze_liked_disliked_products(df):
    """Analyzes the number of positive and negative reviews for each product category."""

    # Filter positive and negative reviews
    positive_reviews = df[df['Sentiment'] == 'positive']
    negative_reviews = df[df['Sentiment'] == 'negative']

    # Count the number of positive reviews by category
    positive_counts = positive_reviews['Class_Name'].value_counts()

    # Count the number of negative reviews by category
    negative_counts = negative_reviews['Class_Name'].value_counts()

    # Combine both into a DataFrame
    liked_disliked_df = pd.DataFrame({
        'Positive_Reviews': positive_counts,
        'Negative_Reviews': negative_counts
    }).fillna(0)  # Fill missing categories with 0

    # Calculate the ratio of positive to negative reviews
    liked_disliked_df['Positive_to_Negative_Ratio'] = liked_disliked_df['Positive_Reviews'] / liked_disliked_df[
        'Negative_Reviews']

    # Return the result sorted by the positive to negative ratio
    return liked_disliked_df.sort_values(by='Positive_to_Negative_Ratio', ascending=False)


# Updated visualization function with color adjustment
def plot_liked_disliked_products(df):
    """Plots the top 10 products with the highest positive to negative ratio."""
    liked_disliked_df = analyze_liked_disliked_products(df)

    # Select top 10 products
    top_10 = liked_disliked_df.head(10)

    # Create the colormap using plt.get_cmap()
    cmap = plt.get_cmap('coolwarm')

    # Plot
    plt.figure(figsize=(10, 6))
    top_10[['Positive_Reviews', 'Negative_Reviews']].plot(kind='bar', stacked=True,
                                                          colormap=cmap)  # Use colormap correctly
    plt.title('Top 10 Products: Positive vs Negative Reviews')
    plt.ylabel('Number of Reviews')
    plt.xlabel('Product Category')
    plt.xticks(rotation=45)
    plt.show()


def plot_low_ratings_by_age(df):
    """Plots the categories with the lowest ratings by age group using a pointplot for better visibility."""

    plt.figure(figsize=(14, 8))  # Augmenter la taille de la figure
    sns.pointplot(data=df, x='Class_Name', y='Rating', hue='Age_Group', palette='coolwarm', dodge=True, markers=["o", "s", "D", "^", "v", "p"])

    plt.title('Lowest Rated Product Categories by Age Group')
    plt.ylabel('Average Rating')
    plt.xlabel('Product Category')
    plt.xticks(rotation=45, ha="right")  # Ajuster l'angle et l'alignement des étiquettes pour les barres
    plt.ylim(0, 5)  # Fixer la limite supérieure de l'axe des Y à 5
    plt.subplots_adjust(bottom=0.2)  # Ajouter de l'espace en bas pour les étiquettes
    plt.legend(title='Age Group', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()  # Assurer que tout rentre bien dans la figure
    plt.show()
