import matplotlib.pyplot as plt
import pandas as pd

# Plot top 10 artists by streams
def plot_top_10_artists(df_top_10_artists):
    plt.figure(figsize=(10, 6))
    plt.bar(df_top_10_artists['artist_name'], df_top_10_artists['total_streams'])
    plt.xlabel('Artist Name')
    plt.ylabel('Total Streams')
    plt.title('Top 10 Artists by Streams')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Plot trends in song releases by year
def plot_release_trends(df_release_trends):
    plt.figure(figsize=(10, 6))
    plt.plot(df_release_trends['released_year'], df_release_trends['song_count'], marker='o')
    plt.xlabel('Year of Release')
    plt.ylabel('Number of Songs Released')
    plt.title('Trends in Song Releases by Year')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plot distribution of songs across platforms
def plot_platform_distribution(df_platform_distribution):
    labels = ['Spotify Playlists', 'Apple Playlists', 'Deezer Playlists']
    sizes = [df_platform_distribution['spotify_playlists'][0], df_platform_distribution['apple_playlists'][0], df_platform_distribution['deezer_playlists'][0]]
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Songs Across Platforms')
    plt.tight_layout()
    plt.show()

# Plot top 10 years with most song releases
def plot_top_10_years_releases(df_top_years_releases):
    plt.figure(figsize=(10, 6))
    plt.bar(df_top_years_releases['released_year'], df_top_years_releases['song_count'])
    plt.xlabel('Year')
    plt.ylabel('Number of Songs Released')
    plt.title('Top 10 Years with Most Song Releases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Plot top artists by playlist and chart presence
def plot_top_artists_playlist_chart(df_top_artists_playlist_chart):
    plt.figure(figsize=(10, 6))
    bar_width = 0.35
    index = range(len(df_top_artists_playlist_chart))

    plt.bar(index, df_top_artists_playlist_chart['spotify_presence'], bar_width, label='Spotify Playlists')
    plt.bar(index, df_top_artists_playlist_chart['apple_presence'], bar_width, bottom=df_top_artists_playlist_chart['spotify_presence'], label='Apple Playlists')

    plt.xlabel('Artist')
    plt.ylabel('Playlist Presence')
    plt.title('Top Artists by Playlist and Chart Presence')
    plt.xticks(index, df_top_artists_playlist_chart['artist_name'], rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
