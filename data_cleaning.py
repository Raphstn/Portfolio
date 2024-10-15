import pandas as pd
import os


# Function to load the raw data
def load_data(file_path):
    """
    Load the raw data from a CSV file.

    Parameters:
    file_path (str): Path to the raw CSV file.

    Returns:
    DataFrame: Loaded data.
    """
    return pd.read_csv(file_path)


# Function to drop unnecessary columns
def drop_columns(df, columns_to_drop):
    """
    Drop the specified columns from the DataFrame.

    Parameters:
    df (DataFrame): The original DataFrame.
    columns_to_drop (list): List of columns to drop.

    Returns:
    DataFrame: DataFrame after dropping specified columns.
    """
    return df.drop(columns=columns_to_drop, errors='ignore')


# Function to check for duplicates
def check_duplicates(df):
    """
    Check for duplicate rows in the DataFrame.

    Parameters:
    df (DataFrame): The DataFrame to check.

    Returns:
    int: Number of duplicate rows.
    """
    return df.duplicated().sum()


# Function to clean data
def clean_data(raw_file_path, cleaned_file_path):
    """
    Cleans the data from the raw CSV file, ensuring all numeric columns contain valid values,
    combines release date columns, and exports cleaned data to a new file.

    Parameters:
    raw_file_path (str): Path to the raw CSV file containing the data.
    cleaned_file_path (str): Path to save the cleaned data.
    """
    # Load raw data
    df = load_data(raw_file_path)

    # Drop unnecessary columns
    columns_to_drop = ['bpm', 'key', 'mode', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%',
                       'instrumentalness_%', 'liveness_%', 'speechiness_%']
    df_cleaned = drop_columns(df, columns_to_drop)

    # Check for duplicates
    duplicates_count = check_duplicates(df_cleaned)
    print(f"Number of duplicate rows: {duplicates_count}")

    # Create 'release_date' column by combining year, month, day
    df_cleaned['release_date'] = pd.to_datetime(df_cleaned['released_year'].astype(str) + '-' +
                                                df_cleaned['released_month'].astype(str) + '-' +
                                                df_cleaned['released_day'].astype(str),
                                                errors='coerce')
    df_cleaned = df_cleaned.dropna(subset=['release_date'])

    # Ensure numeric columns contain valid values
    numeric_columns = ['artist_count', 'streams', 'released_year', 'released_month', 'released_day',
                       'in_spotify_playlists', 'in_spotify_charts', 'in_apple_playlists',
                       'in_apple_charts', 'in_deezer_playlists', 'in_deezer_charts', 'in_shazam_charts']

    for col in numeric_columns:
        df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce').fillna(0).astype(int)

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(cleaned_file_path), exist_ok=True)

    # Save the cleaned DataFrame as an Excel file
    df_cleaned.to_excel(cleaned_file_path, index=False)
    print(f"Cleaned data saved to: {cleaned_file_path}")
