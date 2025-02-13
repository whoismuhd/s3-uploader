import os
import boto3
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch AWS credentials from .env
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")

# Validate AWS credentials
if not all([AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, BUCKET_NAME]):
    raise ValueError("❌ ERROR: Missing AWS environment variables. Check your .env file.")

# Initialize S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this for security

# Route: Home / File Upload
@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        files = request.files.getlist("file")  # Get multiple files
        if files:
            for file in files:
                file.save(file.filename)  # Save locally before upload
                s3_client.upload_file(file.filename, BUCKET_NAME, file.filename)
                os.remove(file.filename)  # Remove local copy
            flash("✅ Files uploaded successfully!", "success")
            return redirect(url_for("upload_file"))

    # Get list of files in S3
    response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
    files = [obj["Key"] for obj in response.get("Contents", [])] if "Contents" in response else []

    return render_template("index.html", files=files)

# Route: Generate Signed URL for File Download
@app.route("/download/<file_name>")
def download_file(file_name):
    try:
        signed_url = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": BUCKET_NAME, "Key": file_name},
            ExpiresIn=3600  # URL expires in 1 hour
        )
        return redirect(signed_url)
    except Exception as e:
        flash(f"❌ Error generating download link: {e}", "danger")
        return redirect(url_for("upload_file"))

# Route: Delete File from S3
@app.route("/delete/<file_name>")
def delete_file(file_name):
    try:
        s3_client.delete_object(Bucket=BUCKET_NAME, Key=file_name)
        flash(f"✅ File '{file_name}' deleted from S3.", "success")
    except Exception as e:
        flash(f"❌ Error deleting file: {e}", "danger")
    return redirect(url_for("upload_file"))


if __name__ == "__main__":
    app.run(debug=True)
