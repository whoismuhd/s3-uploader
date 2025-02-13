import boto3
import os
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

def list_files_in_s3():
    """Lists all files in the S3 bucket."""
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
        if "Contents" in response:
            print("📂 Files in S3 Bucket:")
            for obj in response["Contents"]:
                print(f" - {obj['Key']}")
        else:
            print("📂 No files found in the S3 bucket.")
    except Exception as e:
        print(f"❌ Error fetching file list: {e}")

if __name__ == "__main__":
    list_files_in_s3()
