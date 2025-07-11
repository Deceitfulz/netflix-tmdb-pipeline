from minio import Minio
import os

def upload_to_minio():
    client = Minio(
        "localhost:9000",
        access_key="IhsanTA",
        secret_key="Deceitful112",
        secure=False
    )

    bucket_name = "movies"
    object_name = "processed/movies_joined.parquet"
    local_path = "data/processed/movies_joined.parquet"

    if not os.path.exists(local_path):
        print("❌ File Parquet tidak ditemukan.")
        return

    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
        print(f"✅ Bucket '{bucket_name}' berhasil dibuat.")

    client.fput_object(bucket_name, object_name, local_path)
    print(f"✅ File berhasil di-upload ke MinIO: {bucket_name}/{object_name}")

if __name__ == "__main__":
    upload_to_minio()