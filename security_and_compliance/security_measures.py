```python
# Import necessary libraries
from google.cloud import storage
from google.auth import compute_engine
from google.auth.transport.requests import Request

# Define your Google Cloud Storage bucket name
bucket_name = 'YOUR_BUCKET_NAME'

# Initialize a client for Google Cloud Storage
storage_client = storage.Client()

# Get the bucket from the client
bucket = storage_client.get_bucket(bucket_name)

# Define the IAM policy for the bucket
policy = bucket.get_iam_policy(requested_policy_version=3)

# Define the role for the policy
role = 'roles/storage.objectViewer'

# Define the members for the role
members = [
    'serviceAccount:YOUR_SERVICE_ACCOUNT@YOUR_PROJECT_ID.iam.gserviceaccount.com',
]

# Add the role and members to the policy
policy[role] = members

# Set the IAM policy for the bucket
bucket.set_iam_policy(policy)

# Define the ACL for the bucket
acl = bucket.acl

# Add a user to the ACL
acl.user('YOUR_USER_EMAIL').grant_read()
acl.save()

# Define the default ACL for the bucket
default_acl = bucket.default_object_acl

# Add a user to the default ACL
default_acl.user('YOUR_USER_EMAIL').grant_read()
default_acl.save()

# Function to encrypt data before storing it
def encrypt_data(data):
    # Use Google Cloud KMS to encrypt the data
    # You need to set up a key ring and a key in Google Cloud KMS
    # Replace 'YOUR_KEY_RING', 'YOUR_KEY', and 'YOUR_LOCATION' with your actual values
    key_ring = 'YOUR_KEY_RING'
    key = 'YOUR_KEY'
    location = 'YOUR_LOCATION'

    # Initialize a client for Google Cloud KMS
    kms_client = compute_engine.Credentials.from_service_account_file(
        'YOUR_SERVICE_ACCOUNT_FILE.json',
        scopes=['https://www.googleapis.com/auth/cloud-platform'],
        target_principal='YOUR_SERVICE_ACCOUNT@YOUR_PROJECT_ID.iam.gserviceaccount.com',
        target_scopes=['https://www.googleapis.com/auth/cloud-platform'],
    )

    # Get the key name
    key_name = kms_client.crypto_key_path_path('YOUR_PROJECT_ID', location, key_ring, key)

    # Encrypt the data
    response = kms_client.encrypt(key_name, data)

    # Return the encrypted data
    return response.ciphertext

# Function to decrypt data after retrieving it
def decrypt_data(ciphertext):
    # Use Google Cloud KMS to decrypt the data
    # You need to set up a key ring and a key in Google Cloud KMS
    # Replace 'YOUR_KEY_RING', 'YOUR_KEY', and 'YOUR_LOCATION' with your actual values
    key_ring = 'YOUR_KEY_RING'
    key = 'YOUR_KEY'
    location = 'YOUR_LOCATION'

    # Initialize a client for Google Cloud KMS
    kms_client = compute_engine.Credentials.from_service_account_file(
        'YOUR_SERVICE_ACCOUNT_FILE.json',
        scopes=['https://www.googleapis.com/auth/cloud-platform'],
        target_principal='YOUR_SERVICE_ACCOUNT@YOUR_PROJECT_ID.iam.gserviceaccount.com',
        target_scopes=['https://www.googleapis.com/auth/cloud-platform'],
    )

    # Get the key name
    key_name = kms_client.crypto_key_path_path('YOUR_PROJECT_ID', location, key_ring, key)

    # Decrypt the data
    response = kms_client.decrypt(key_name, ciphertext)

    # Return the decrypted data
    return response.plaintext
```
