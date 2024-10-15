
import pandas as pd
from sqlalchemy import create_engine

# Function to execute a query and return the result as a DataFrame
def query_to_dataframe(query, conn_string):
    engine = create_engine(conn_string)
    with engine.connect() as conn:
        return pd.read_sql_query(query, conn)

# Function to get top 10 artists by streams
def get_top_10_artists(conn_string):
    query_top_10_artists = """
    SELECT artist_name, SUM(streams) as total_streams
    FROM spotify_songs
    GROUP BY artist_name
    ORDER BY total_streams DESC
    LIMIT 10;
    """
    return query_to_dataframe(query_top_10_artists, conn_string)

# Function to get trends in song releases by year
def get_release_trends(conn_string):
    query_release_trends = """
    SELECT released_year, COUNT(*) as song_count
    FROM spotify_songs
    GROUP BY released_year
    ORDER BY released_year;
    """
    return query_to_dataframe(query_release_trends, conn_string)

# Function to get distribution of songs across platforms
def get_platform_distribution(conn_string):
    query_platform_distribution = """
    SELECT
        SUM(in_spotify_playlists) as spotify_playlists,
        SUM(in_apple_playlists) as apple_playlists,
        SUM(in_deezer_playlists) as deezer_playlists
    FROM spotify_songs;
    """
    return query_to_dataframe(query_platform_distribution, conn_string)

# Function to get top 10 years with most song releases
def get_top_10_years_releases(conn_string):
    query_top_years = """
    SELECT released_year, COUNT(*) as song_count
    FROM spotify_songs
    GROUP BY released_year
    ORDER BY song_count DESC
    LIMIT 10;
    """
    return query_to_dataframe(query_top_years, conn_string)


# Function to get top artists by presence in playlists and charts
def get_top_artists_playlist_chart(conn_string):
    query_top_artists_playlist_chart = """
    SELECT artist_name, SUM(in_spotify_playlists) as spotify_presence, SUM(in_apple_playlists) as apple_presence, SUM(streams) as total_streams
    FROM spotify_songs
    GROUP BY artist_name
    ORDER BY total_streams DESC
    LIMIT 10;
    """
    return query_to_dataframe(query_top_artists_playlist_chart, conn_string)

