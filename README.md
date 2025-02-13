S3 Uploader Web App 🚀
A simple web application to upload, download, and manage files on AWS S3. Built with Flask, Dropzone.js, and Bootstrap for an intuitive drag-and-drop file upload experience.

🌟 Features
✅ Drag & Drop File Uploads
✅ Multiple File Uploads
✅ Download and Delete Files
✅ Progress Bar for Uploads
✅ Animated Gradient UI
✅ AWS S3 Storage Integration


📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/whoismuhd/s3-uploader.git
cd s3-uploader


2️⃣ Create a Virtual Environment (not necessary but my personal recommendation)
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows


3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Set Up Environment Variables
Create a .env file:
touch .env

5 Add your AWS credentials inside .env:
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=eu-central-1
AWS_S3_BUCKET_NAME=your-bucket-name


🛠 Usage
Drag & Drop files into the upload area.
Monitor the progress bar for real-time upload feedback.
View uploaded files in the list.
Download files with a single click.
Delete files from S3 securely.



🔐 Security Considerations
NEVER expose .env or AWS credentials in GitHub.
Use AWS IAM roles instead of static access keys if possible.
Limit S3 bucket permissions to only required actions.


📜 License
This project is open-source and available under the MIT License.


👨‍💻 Author
Developed by whoismuhd
For questions or contributions, open an issue or pull request on GitHub.

