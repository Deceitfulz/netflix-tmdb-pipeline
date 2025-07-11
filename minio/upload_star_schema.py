from minio import Minio
import os

client = Minio(
    "localhost:9000",
    access_key="IhsanTA",
    secret_key="Deceitful112",
    secure=False
)

bucket = "movies"
folder = "star_schema/"
local_dir = "data/star_schema"

def upload_file(local_file):
    object_name = f"{folder}{os.path.basename(local_file)}"
    client.fput_object(bucket, object_name, local_file)
    print(f"✅ Uploaded: {bucket}/{object_name}")

def main():
    if not client.bucket_exists(bucket):
        client.make_bucket(bucket)
        print(f"✅ Bucket '{bucket}' created.")

    for file in os.listdir(local_dir):
        if file.endswith(".parquet"):
            upload_file(os.path.join(local_dir, file))

if __name__ == '__main__':
    main()