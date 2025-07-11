import streamlit as st
import pandas as pd

st.set_page_config(page_title="Netflix + TMDB Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_parquet("data/processed/movies_joined.parquet")
    return df.dropna(subset=['vote_average', 'runtime'])

df = load_data()

st.title("🎬 Netflix + TMDB Movie Dashboard")

# Sidebar filter
with st.sidebar:
    selected_type = st.selectbox("Pilih Tipe Konten", df['type'].unique())
    min_year, max_year = int(df['release_year'].min()), int(df['release_year'].max())
    selected_year = st.slider("Tahun Rilis", min_year, max_year, (min_year, max_year))

filtered_df = df[
    (df['type'] == selected_type) &
    (df['release_year'] >= selected_year[0]) &
    (df['release_year'] <= selected_year[1])
]

st.markdown(f"### Top 10 {selected_type} berdasarkan Rating")
top10 = filtered_df.sort_values("vote_average", ascending=False).head(10)
st.dataframe(top10[['title', 'release_year', 'genre_netflix', 'vote_average', 'runtime']])

# Chart popularitas film
st.markdown("### Distribusi Popularitas per Tahun")
popularity_by_year = filtered_df.groupby('release_year')['popularity'].mean().reset_index()

st.line_chart(popularity_by_year, x='release_year', y='popularity')

# Distribusi genre
st.markdown("### Distribusi Genre (Netflix Listed In)")
st.bar_chart(filtered_df['genre_netflix'].value_counts().head(10))