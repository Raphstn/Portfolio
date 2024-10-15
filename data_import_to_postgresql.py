
import pandas as pd
import psycopg2


def import_data_to_postgresql(cleaned_file_path):
    """
    Imports cleaned data from an Excel file into a PostgreSQL database.

    Parameters:
    cleaned_file_path (str): Path to the cleaned data file.
    """
    # Load cleaned data
    data_excel = pd.read_excel(cleaned_file_path)

    # Print some rows to verify release_date before importing
    print("Sample release_date values before import:")
    print(data_excel[['track_name', 'release_date']].head())

    # Print data types of each column
    print("Data types of each column before import:")
    print(data_excel.dtypes)

    # Check for missing values
    print("Missing values in columns before import:")
    print(data_excel.isnull().sum())

    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",  # Adjust as needed
        database="spotify_db",  # Your database name
        user="postgres",  # Your PostgreSQL username
        password="Coupine2303"  # Your PostgreSQL password
    )
    cur = conn.cursor()

    # Clear the existing data to avoid duplication
    cur.execute("DELETE FROM spotify_songs;")
    conn.commit()

    # SQL insert query
    insert_query = """
       INSERT INTO spotify_songs (
           track_name, artist_name, artist_count, released_year, released_month, 
           released_day, in_spotify_playlists, in_spotify_charts, streams, 
           in_apple_playlists, in_apple_charts, in_deezer_playlists, in_deezer_charts, 
           in_shazam_charts, release_date
       ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
       """
    # Insert data into PostgreSQL
    for index, row in data_excel.iterrows():
        # Insert the row into PostgreSQL
        cur.execute(insert_query, (
            row['track_name'], row['artist(s)_name'], row['artist_count'], row['released_year'],
            row['released_month'], row['released_day'], row['in_spotify_playlists'], row['in_spotify_charts'],
            row['streams'], row['in_apple_playlists'], row['in_apple_charts'], row['in_deezer_playlists'],
            row['in_deezer_charts'], row['in_shazam_charts'], row['release_date']
        ))

    # Commit changes
    conn.commit()

    # Verify the number of rows inserted
    cur.execute("SELECT COUNT(*) FROM spotify_songs;")
    row_count = cur.fetchone()[0]
    print(f"Number of rows successfully inserted: {row_count}")

    # Close the connection
    cur.close()
    conn.close()

