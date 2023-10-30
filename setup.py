from setuptools import setup, find_packages

setup(
    name='fileuploader',
    version='1.0.0',
    description='File uploader for AWS S3 and GCS',
    zip_safe=False,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    python_requires = ">=3.6"
)