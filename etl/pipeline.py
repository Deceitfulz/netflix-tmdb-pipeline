from etl.transform import clean_and_merge
from etl.load import save_parquet

def run_pipeline():
    print("🚀 Menjalankan ETL pipeline...")
    df = clean_and_merge()
    save_parquet(df)
    print("🎉 ETL selesai!")


if __name__ == '__main__':
    run_pipeline()