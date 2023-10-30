import os 

from  src.uploader import upload_files_in_directory
# Get the current script's directory
current_dir = os.path.dirname(__file__)

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
dir_path = project_root + "\\upload_files"
upload_files_in_directory(dir_path)