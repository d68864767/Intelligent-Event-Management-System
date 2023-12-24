```python
# Import necessary libraries
from google.cloud import storage

# Define Google Cloud project and bucket details
project_id = 'YOUR_PROJECT_ID'
bucket_name = 'YOUR_BUCKET_NAME'

# Initialize a client for Cloud Storage
client = storage.Client(project=project_id)

# Get the bucket
bucket = client.get_bucket(bucket_name)

def upload_file(file_path, destination_blob_name):
    """
    Function to upload a file to Google Cloud Storage
    :param file_path: Path to the file
    :param destination_blob_name: Name of the blob in the bucket
    """
    # Create a blob in the bucket
    blob = bucket.blob(destination_blob_name)

    # Upload the file to the blob
    blob.upload_from_filename(file_path)

    print(f"File {file_path} uploaded to {destination_blob_name}.")

def download_file(source_blob_name, destination_file_name):
    """
    Function to download a file from Google Cloud Storage
    :param source_blob_name: Name of the blob in the bucket
    :param destination_file_name: Path to save the downloaded file
    """
    # Get the blob from the bucket
    blob = bucket.blob(source_blob_name)

    # Download the blob to a file
    blob.download_to_filename(destination_file_name)

    print(f"File {source_blob_name} downloaded to {destination_file_name}.")

def delete_file(blob_name):
    """
    Function to delete a file from Google Cloud Storage
    :param blob_name: Name of the blob in the bucket
    """
    # Get the blob from the bucket
    blob = bucket.blob(blob_name)

    # Delete the blob
    blob.delete()

    print(f"File {blob_name} deleted.")
```
