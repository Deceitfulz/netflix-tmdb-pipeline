import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import os

df = pd.read_parquet("data/processed/movies_joined.parquet")

# 🔹 Dim Movie
dim_movie = df[['title', 'type', 'country', 'release_year', 'description', 'runtime']].drop_duplicates().reset_index(drop=True)
dim_movie['MovieId'] = dim_movie.index + 1

# 🔹 Dim Genre
dim_genre = df[['genre_netflix', 'genre_tmdb']].drop_duplicates().reset_index(drop=True)
dim_genre['GenreId'] = dim_genre.index + 1

# 🔹 Dim Date (berdasarkan release_year)
dim_date = df[['release_year']].drop_duplicates().reset_index(drop=True)
dim_date['DateId'] = dim_date.index + 1
dim_date['Year'] = dim_date['release_year']
dim_date['Quarter'] = ((dim_date['Year'] - dim_date['Year'].min()) % 4) + 1
dim_date['Semester'] = ((dim_date['Year'] - dim_date['Year'].min()) % 2) + 1

# 🔹 Faktanya
fact = df.merge(dim_movie, on=['title', 'type', 'country', 'release_year', 'description', 'runtime'])
fact = fact.merge(dim_genre, on=['genre_netflix', 'genre_tmdb'])
fact = fact.merge(dim_date, on=['release_year'])
fact_movies = fact[['MovieId', 'GenreId', 'DateId', 'vote_average', 'vote_count', 'popularity']]

# 🔹 Simpan
os.makedirs("data/star_schema/", exist_ok=True)

dim_movie.to_parquet("data/star_schema/dim_movie.parquet", index=False)
dim_genre.to_parquet("data/star_schema/dim_genre.parquet", index=False)
dim_date.to_parquet("data/star_schema/dim_date.parquet", index=False)
fact_movies.to_parquet("data/star_schema/fact_movies.parquet", index=False)

print("✅ Star Schema berhasil dibuat dan disimpan.")