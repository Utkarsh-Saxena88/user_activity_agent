import firebase_admin
from firebase_admin import credentials, storage
import os

class FirebaseUploader:
    def __init__(self, cred_path, bucket_name):
        # Initialize the Firebase Admin SDK
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred, {'storageBucket': bucket_name})

        self.bucket = storage.bucket()

    def upload_file(self, file_path):
        try:
            filename = os.path.basename(file_path)
            blob = self.bucket.blob(filename)
            blob.upload_from_filename(file_path)
            print(f"Uploaded {filename} to Firebase Storage")
        except Exception as e:
            print(f"Error uploading file: {e}")
