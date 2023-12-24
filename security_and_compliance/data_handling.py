```python
# Import necessary libraries
from google.cloud import storage
from google.cloud import secretmanager

# Define your Google Cloud project details
project_id = 'YOUR_PROJECT_ID'
bucket_name = 'YOUR_BUCKET_NAME'
secret_id = 'YOUR_SECRET_ID'
version_id = 'latest'

# Initialize the client for Secret Manager
secret_client = secretmanager.SecretManagerServiceClient()

# Get the full path of the secret
secret_name = secret_client.secret_version_path(project_id, secret_id, version_id)

# Access the secret
response = secret_client.access_secret_version(secret_name)

# Get the secret key
secret_key = response.payload.data.decode('UTF-8')

# Initialize the client for Cloud Storage
storage_client = storage.Client()

# Get the bucket
bucket = storage_client.get_bucket(bucket_name)

def store_data(data, file_name):
    """
    Function to store data in Google Cloud Storage
    :param data: Data to be stored
    :param file_name: Name of the file in which data will be stored
    """
    # Create a new blob and upload the file
    blob = bucket.blob(file_name)
    blob.upload_from_string(data)

    # Set the blob to be private
    blob.make_private()

def retrieve_data(file_name):
    """
    Function to retrieve data from Google Cloud Storage
    :param file_name: Name of the file from which data will be retrieved
    :return: Retrieved data
    """
    # Get the blob
    blob = bucket.get_blob(file_name)

    # Download the blob as a string
    data = blob.download_as_text()

    return data

def delete_data(file_name):
    """
    Function to delete data from Google Cloud Storage
    :param file_name: Name of the file to be deleted
    """
    # Get the blob
    blob = bucket.get_blob(file_name)

    # Delete the blob
    blob.delete()

def encrypt_data(data):
    """
    Function to encrypt data using the secret key
    :param data: Data to be encrypted
    :return: Encrypted data
    """
    # Use the secret key to encrypt the data
    encrypted_data = ''.join(chr(ord(c) ^ ord(secret_key[i % len(secret_key)])) for i, c in enumerate(data))

    return encrypted_data

def decrypt_data(encrypted_data):
    """
    Function to decrypt data using the secret key
    :param encrypted_data: Data to be decrypted
    :return: Decrypted data
    """
    # Use the secret key to decrypt the data
    decrypted_data = ''.join(chr(ord(c) ^ ord(secret_key[i % len(secret_key)])) for i, c in enumerate(encrypted_data))

    return decrypted_data
```
