import os
from src.uploader import upload_to_s3,upload_to_gcs

# Define a test directory and files for testing
# Get the current script's directory
current_dir = os.path.dirname(__file__)

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
TEST_DIR = project_root + "\\test_upload_files"
TEST_FILES = [
    "test_image.jpg",
    "test_document.docx",
    "test_text.txt",
    "test_video.mp4",
]

def create_test_files():
    os.makedirs(TEST_DIR, exist_ok=True)
    for file in TEST_FILES:
        with open(os.path.join(TEST_DIR, file), "w") as f:
            f.write("Test file content")

def test_upload_to_s3():
    create_test_files()
    for file in TEST_FILES:
        uploaded = upload_to_s3(file, os.path.join(TEST_DIR, file))
        assert uploaded is None  # Replace with actual assertion

def test_upload_to_gcs():
    create_test_files()
    for file in TEST_FILES:
        uploaded = upload_to_gcs(file, os.path.join(TEST_DIR, file))
        assert uploaded is None  # Replace with actual assertion

if __name__ == "__main__":
    create_test_files()  # Ensure test files exist
    import pytest
    pytest.main()
