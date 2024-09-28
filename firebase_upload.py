import firebase_admin
from firebase_admin import credentials, storage
import os
import requests
import time

class FirebaseUploader:
    def __init__(self, cred_path, bucket_name):
        # Check if the default app has already been initialized
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred, {
                'storageBucket': bucket_name
            })
        self.bucket = storage.bucket(bucket_name)

        self.upload_queue = []  # Store failed uploads here

    def check_internet_connection(self):
        """Check if the internet connection is active."""
        try:
            requests.get("https://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False

    def upload_file(self, file_path):
        """Upload file to Firebase Storage."""
        blob = self.bucket.blob(os.path.basename(file_path))
        try:
            # Check if the internet is connected
            if self.check_internet_connection():
                blob.upload_from_filename(file_path)
                print(f"Successfully uploaded {file_path} to Firebase Storage.")
            else:
                print(f"No internet connection. Queuing {file_path} for retry.")
                self.upload_queue.append(file_path)
        except Exception as e:
            print(f"Error uploading {file_path}: {e}")
            if "firewall" in str(e).lower():
                print("Possible firewall issue detected. Please check your network settings.")
            self.upload_queue.append(file_path)

    def retry_queued_uploads(self):
        """Retry uploading files from the queue."""
        for file_path in list(self.upload_queue):  # Create a copy of the list
            print(f"Retrying upload for {file_path}...")
            self.upload_file(file_path)
            if file_path not in self.upload_queue:
                self.upload_queue.remove(file_path)

    def save_queue(self, file_path='upload_queue.txt'):
        """Save the queue to a file before application shutdown."""
        with open(file_path, 'w') as f:
            for item in self.upload_queue:
                f.write(f"{item}\n")
        print(f"Upload queue saved to {file_path}.")

    def load_queue(self, file_path='upload_queue.txt'):
        """Load the upload queue from a file at startup."""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                self.upload_queue = f.read().splitlines()
            print(f"Loaded {len(self.upload_queue)} items from upload queue.")

    def shutdown_handler(self):
        """Handle safe shutdown for pending uploads."""
        if self.upload_queue:
            print("Application is shutting down. Saving pending uploads...")
            self.save_queue()

