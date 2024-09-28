import firebase_admin
from firebase_admin import credentials, storage
import os

class FirebaseUploader:
    def __init__(self, cred_path, bucket_name):
        # Initialize Firebase with credentials and bucket
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred, {
                'storageBucket': bucket_name
            })
        self.bucket = storage.bucket()

    def upload_file(self, file_path):
        # Get the file name from the path
        file_name = os.path.basename(file_path)
        
        # Create a blob (file object) in Firebase storage
        blob = self.bucket.blob(file_name)

        # Upload the file to Firebase Storage
        blob.upload_from_filename(file_path)
        
        # Optionally, you can make the file publicly accessible
        blob.make_public()

        print(f"File {file_name} uploaded to Firebase Storage and made public.")
