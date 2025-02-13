import boto3
import os
import argparse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch AWS credentials
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")

# Initialize S3 Client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def upload_file_to_s3(file_path, bucket_name, object_name=None):
    """Uploads a file to an S3 bucket."""
    if not os.path.isfile(file_path):
        print(f"❌ Error: The file '{file_path}' does not exist!")
        return
    
    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"✅ File '{file_path}' uploaded to S3 bucket '{bucket_name}' as '{object_name}'.")
    except Exception as e:
        print(f"❌ Error uploading file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a file to AWS S3.")
    parser.add_argument("file_path", type=str, help="Path of the file to upload.")
    parser.add_argument("--object_name", type=str, help="S3 object name (optional).")

    args = parser.parse_args()

    upload_file_to_s3(args.file_path, BUCKET_NAME, args.object_name)
