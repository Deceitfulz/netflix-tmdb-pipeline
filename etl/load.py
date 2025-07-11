import pyarrow as pa
import pyarrow.parquet as pq
import os
from etl import config

def save_parquet(df):
    os.makedirs(config.PROCESSED_PATH, exist_ok=True)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, config.JOINED_FILE, compression='zstd')
    print(f"✅ File berhasil disimpan di {config.JOINED_FILE}")