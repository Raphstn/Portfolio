def calculate_age_rating_correlation(df):
    """Calculates and returns the correlation between age and ratings."""
    correlation = df['Age'].corr(df['Rating'])
    return correlation

def describe_numerical_columns(df):
    """Returns summary statistics for numerical columns."""
    return df.describe()

def count_unique_values(df):
    """Counts and prints the number of unique values for key categorical columns."""
    print(f"{df['Class_Name'].nunique()} unique product categories")
    print(f"{df['Division_Name'].nunique()} unique divisions")
    print(f"{df['Rating'].nunique()} unique rating values")


def analyze_low_ratings_by_age(df, threshold=4.0):
    """Analyzes categories with the lowest average ratings by age group."""

    # Group by Age Group and Class Name, and calculate the average rating for each group
    low_ratings_by_age = df.groupby(['Age_Group', 'Class_Name'])['Rating'].mean().reset_index()

    # Filter for categories with ratings below the specified threshold
    low_ratings_by_age = low_ratings_by_age[low_ratings_by_age['Rating'] < threshold]

    # Sort by Age Group and Ratings to see the lowest ratings by group
    return low_ratings_by_age.sort_values(by=['Age_Group', 'Rating'], ascending=True)


