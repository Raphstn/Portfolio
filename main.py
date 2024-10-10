import pandas as pd
import os
from Utils.data_cleaning import drop_columns, check_duplicates, load_data


df = load_data('/Users/raphaelstanislas/Desktop/Portfolio Data Analysis/Spotify Sreamed Songs/Data/Brut/Spotify Most Streamed Songs.csv')
# print(df.head())
# print(df.isnull().sum())
print(df.columns)

# # List of columns to drop
columns_to_drop = ['bpm', 'key', 'mode', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%' ]
# Call the function to drop the columns
df_cleaned = drop_columns(df, columns_to_drop)
print(df_cleaned.dtypes)

# Check for duplicates
duplicates_count = check_duplicates(df)
print(f"Number of duplicate rows: {duplicates_count}")#
# Assuming df_cleaned is already defined and cleaned
# Combine 'released_year', 'released_month', and 'released_day' into a single string for df_cleaned
df_cleaned['release_date'] = pd.to_datetime(df_cleaned['released_year'].astype(str) + '-' +
                                            df_cleaned['released_month'].astype(str) + '-' +
                                            df_cleaned['released_day'].astype(str))

# Check the result
print(df_cleaned[['released_year', 'released_month', 'released_day', 'release_date']].head())

print(df_cleaned.info())
df_cleaned['in_deezer_playlists'] = pd.to_numeric(df['in_deezer_playlists'], errors='coerce').fillna(0).astype(int)
df_cleaned['in_shazam_charts'] = pd.to_numeric(df['in_shazam_charts'], errors='coerce').fillna(0).astype(int)
print(df_cleaned.info())


# Create the directory if it doesn't exist
os.makedirs("Data/Processed", exist_ok=True)

# Save the DataFrame as an Excel file
df_cleaned.to_excel("Data/Processed/df_cleaned.xlsx", index=False)
