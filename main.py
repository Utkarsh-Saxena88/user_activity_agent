import time
import os
from activity_tracker import ActivityTracker
from firebase_upload import FirebaseUploader
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
# cred = credentials.Certificate('config/db-firebase-credentials.json')
# firebase_admin.initialize_app(cred)

db = firestore.client()

# Initialize Firebase uploader
firebase_uploader = FirebaseUploader(
    cred_path='config/db-firebase-credentials.json', 
    bucket_name='user-activity-db.appspot.com'
)

# Directory where screenshots will be saved before uploading
screenshot_directory = 'screenshots'
if not os.path.exists(screenshot_directory):
    os.makedirs(screenshot_directory)

def main():
    # Initialize the ActivityTracker
    tracker = ActivityTracker()

    # Poll for configuration updates
    try:
        # Prompt for configuration update only once at the start
        if input("Do you want to update configuration? (yes/no): ").strip().lower() == "yes":
            tracker.update_config()
        
        while True:
            screenshot_path = tracker.track_user_activity()

            if screenshot_path:  # Check if a valid screenshot path was returned
                try:
                    # Upload the screenshot to Firebase
                    firebase_uploader.upload_file(screenshot_path)
                    print(f"Uploaded {screenshot_path} to Firebase.")

                    # Optionally delete local screenshot after upload
                    if os.path.exists(screenshot_path):
                        os.remove(screenshot_path)
                        print(f"Deleted local file: {screenshot_path}")

                except Exception as e:
                    print(f"Failed to upload {screenshot_path} to Firebase: {e}")

            # Wait for the user-defined screenshot interval before tracking again
            time.sleep(tracker.screenshot_interval)
    
    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting gracefully.")

if __name__ == "__main__":
    main()
