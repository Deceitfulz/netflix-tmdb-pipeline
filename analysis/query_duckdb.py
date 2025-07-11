import duckdb

def main():
    parquet_path = 'data/processed/movies_joined.parquet'
    
    con = duckdb.connect()

    print("🔍 Menjalankan query analitik...")
    query = f'''
    SELECT
        genre_netflix,
        COUNT(*) AS total_movies,
        ROUND(AVG(vote_average), 2) AS avg_rating,
        ROUND(AVG(runtime), 1) AS avg_runtime
    FROM read_parquet('{parquet_path}')
    GROUP BY genre_netflix
    ORDER BY avg_rating DESC
    LIMIT 10
    '''

    df = con.execute(query).df()
    print("\n🎯 Genre Netflix dengan rating tertinggi:")
    print(df)

if __name__ == '__main__':
    main()