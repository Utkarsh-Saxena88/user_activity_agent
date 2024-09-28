import os
import firebase_admin
from firebase_admin import credentials, storage

class FirebaseUploader:
    def __init__(self, cred_path, bucket_name):
        # Check if the default app has already been initialized
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred, {
                'storageBucket': bucket_name
            })
        self.bucket = storage.bucket(bucket_name)

    def upload_file(self, file_path):
        """Upload a file to Firebase Storage."""
        blob = self.bucket.blob(os.path.basename(file_path))
        blob.upload_from_filename(file_path)
        print(f"Uploaded {file_path} to Firebase Storage.")
