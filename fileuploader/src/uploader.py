import os
import boto3
from google.cloud import storage

# AWS S3 Configuration
aws_access_key = 'AWS_ACCESS_KEY'
aws_secret_key = 'AWS_SECRET_KEY'
aws_bucket_name = 's3-bucket-name'
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# Google Cloud Storage Configuration
gcs_bucket_name = 'file-upload'
gcs_client = storage.Client()

# Define the allowed file types for each cloud storage service

s3_allowed_types = ('.jpg','.jpeg','.png', '.webp', '.mpeg', '.3gpp', '.mp3', '.3gp', '.wmv', '.mp4', '.webm')
gcs_allowed_types = ('.doc', '.docx', '.pdf', '.csv')

def upload_to_s3(filename, file_path):
    if filename.endswith(s3_allowed_types): # Upload to AWS S3 if it's an image or media file
        # print("s3 files: ", file_path)        
        s3_client.upload_file(file_path, aws_bucket_name, os.path.basename(file_path))
    

def upload_to_gcs(filename, file_path):
    if filename.endswith(gcs_allowed_types): # Upload to Google Cloud Storage if it's a document
        # print("gcs files: ",file_path)        
        bucket = gcs_client.get_bucket(gcs_bucket_name)
        blob = bucket.blob(os.path.basename(file_path))
        blob.upload_from_filename(file_path)

def upload_files_in_directory(dir_path):
    for root, _, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                upload_to_s3(file, file_path)  
                upload_to_gcs(file, file_path)  

def _main():
    current_dir = os.path.dirname(__file__)
    # Add the project root directory to the Python path
    project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
    dir_path = project_root + "\\test_upload_files"
    upload_files_in_directory(dir_path)

if __name__ == "__main__":
    _main()
