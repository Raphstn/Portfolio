import pandas as pd


def load_data(filepath):
    """Loads the dataset from a CSV file."""
    df = pd.read_csv(filepath)
    return df


def clean_data(df):
    """Performs data cleaning operations."""
    # Rename columns for easier manipulation
    df_cleaned = df.rename(columns={
        'Clothing ID': 'Clothing_ID',
        'Review Text': 'Review_Text',
        'Recommended IND': 'Recommended',
        'Positive Feedback Count': 'Positive_Feedback_Count',
        'Division Name': 'Division_Name',
        'Department Name': 'Department_Name',
        'Class Name': 'Class_Name'
    })

    # Drop unnecessary columns
    df_cleaned = df_cleaned.drop(columns=['Title', 'Unnamed: 0'])

    # Fill missing values in 'Review_Text'
    df_cleaned['Review_Text'] = df_cleaned['Review_Text'].fillna('No Review')

    # Drop rows with missing values in key columns
    df_cleaned = df_cleaned.dropna(subset=['Division_Name', 'Department_Name', 'Class_Name'])

    return df_cleaned
