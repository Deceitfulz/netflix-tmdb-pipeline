import pandas as pd
from etl import config

def clean_and_merge():
    # Load dataset
    netflix = pd.read_csv(config.NETFLIX_FILE)
    tmdb = pd.read_csv(config.TMDB_FILE)

    # Bersihkan dan normalisasi kolom judul
    netflix['title_clean'] = netflix['title'].str.lower().str.strip()
    tmdb['title_clean'] = tmdb['title'].str.lower().str.strip()

    # Ubah genre menjadi string dari list
    tmdb['genre_tmdb'] = tmdb['genres'].apply(lambda x: ', '.join([g['name'] for g in eval(x)]) if pd.notna(x) else None)
    netflix['genre_netflix'] = netflix['listed_in']

    # Gabungkan berdasarkan title_clean
    merged = pd.merge(netflix, tmdb, on='title_clean', how='inner', suffixes=('_netflix', '_tmdb'))

    # Pilih kolom hasil akhir
    merged_final = merged.copy()
    merged_final['title'] = merged['title_netflix']
    merged_final = merged_final[config.SELECTED_COLUMNS]

    return merged_final