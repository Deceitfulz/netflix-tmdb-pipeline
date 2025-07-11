import os

# Konfigurasi path
RAW_PATH = "data/raw/"
PROCESSED_PATH = "data/processed/"
JOINED_FILE = os.path.join(PROCESSED_PATH, "movies_joined.parquet")

# Nama file
NETFLIX_FILE = os.path.join(RAW_PATH, "netflix_titles.csv")
TMDB_FILE = os.path.join(RAW_PATH, "tmdb_5000_movies.csv")

# Kolom hasil gabungan yang akan disimpan
SELECTED_COLUMNS = [
    'title', 'type', 'release_year', 'country', 'genre_netflix', 'description',
    'popularity', 'vote_average', 'vote_count', 'runtime', 'genre_tmdb'
]