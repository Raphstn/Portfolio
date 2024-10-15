# ***Spotify Most Streamed Songs Analysis***

## ***Project Overview***
This project is an in-depth analysis of the most streamed songs on Spotify, focusing on understanding key trends and insights about music releases and popularity. The data was cleaned, processed, and imported into a PostgreSQL database, and further explored using Python and visualized with Tableau.

## ***Objectives***
The main objectives of this project are:

1. **Data Cleaning & Importation**:
   - Clean the raw dataset to make it ready for analysis.
   - Import the cleaned dataset into a PostgreSQL database.

2. **Data Analysis**:
   - Generate meaningful insights into the trends and characteristics of popular songs.
   - Analyze top artists, release trends, and platform distribution.

3. **Visualization**:
   - Create clear visualizations to communicate findings effectively, using Python and Tableau.

## ***Project Structure***
- `main.py`: The main script that orchestrates the project by loading data, cleaning it, performing analysis, and visualizing the results.
- `data_cleaning.py`: Contains functions to load and clean the dataset (handle missing values, rename columns, etc.).
- `data_visualization.py`: Contains functions to generate various data visualizations (top artists by streams, trends in song releases, etc.).
- `data_analysis.py`: Performs statistical analyses such as calculating trends and platform distributions.
- `data/`: Directory containing the raw dataset (`Spotify_Most_Streamed_Songs.csv`) and the cleaned dataset (`cleaned_data.csv`).

## ***Technologies and Libraries Used***
The following technologies and Python libraries were used in this project:

- **Python**: Main programming language for data cleaning, manipulation, and analysis.
- **pandas**: For data cleaning, manipulation, and handling missing values.
- **numpy**: For numerical operations and handling arrays.
- **matplotlib**: For plotting and visual representation of data.
- **PostgreSQL**: Used to store and manage the cleaned dataset, enabling structured queries and analysis.
- **SQLAlchemy**: Utilized to facilitate interaction between Python and PostgreSQL.
- **Tableau**: To create interactive and insightful visual dashboards for communicating findings.

## ***Dataset Overview***
The dataset used in this project is provided in the `data/` directory and includes the following columns:

- **Track Name**: Name of the song.
- **Artist Name**: Name of the artist.
- **Artist Count**: Number of artists featured in the song.
- **Released Year**: Year the song was released.
- **Released Month**: Month the song was released.
- **Released Day**: Day the song was released.
- **Streams**: Number of times the song was streamed on Spotify.
- **In Spotify Playlists**: Number of Spotify playlists the song is included in.
- **In Apple Playlists**: Number of Apple Music playlists the song is included in.
- **In Deezer Playlists**: Number of Deezer playlists the song is included in.
- **In Shazam Charts**: Number of Shazam charts the song has appeared in.

## ***Key Insights***
Some key insights derived from the analysis include:

1. **Top 10 Artists by Streams**:
   - Artists such as The Weeknd, Taylor Swift, and Ed Sheeran have dominated Spotify streams, reflecting their broad global appeal.

2. **Trends in Song Releases**:
   - The number of song releases has increased dramatically over the last few years, peaking around 2020-2023. This trend is likely influenced by digital platform growth and the global pandemic, which led to more digital music consumption.

3. **Platform Distribution**:
   - A majority (96.9%) of songs are featured on Spotify playlists, showing its dominance over other streaming platforms like Apple Music and Deezer.

4. **Artists' Playlist Presence**:
   - Top artists like The Weeknd and Taylor Swift have strong representation across multiple platforms, which contributes to their high streaming numbers.

## ***Recommendations***

1. **Focus on Cross-Platform Promotion**:
   - Increase efforts to promote songs across multiple platforms to enhance streaming numbers, especially on platforms where presence is low (e.g., Apple Music, Deezer).

2. **Targeted Release Strategy**:
   - Artists can optimize their song releases during months with historically higher engagement, such as the late months of the year.

3. **Leverage Playlist Inclusion**:
   - Focus on securing inclusion in popular playlists, as they contribute significantly to the streaming numbers of top artists.

## ***Installation Instructions***
To run this project on your local machine, follow the steps below:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Raphstn/Spotify_Streamed_Songs.git
