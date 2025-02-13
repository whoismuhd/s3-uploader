import boto3
import os
import argparse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")

# Initialize S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def delete_file_from_s3(file_name, bucket_name):
    """Deletes a file from an S3 bucket."""
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        print(f"✅ File '{file_name}' deleted from S3 bucket '{bucket_name}'.")
    except Exception as e:
        print(f"❌ Error deleting file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete a file from AWS S3.")
    parser.add_argument("file_name", type=str, help="The name of the file to delete from S3.")

    args = parser.parse_args()
    delete_file_from_s3(args.file_name, BUCKET_NAME)
