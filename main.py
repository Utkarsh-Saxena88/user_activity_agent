from activity_tracker import ActivityTracker
from firebase_upload import FirebaseUploader
import time
import os

# Initialize Firebase uploader
firebase_uploader = FirebaseUploader(
    cred_path='config/firebase_credentials.json', 
    bucket_name='user-activity-agent.appspot.com'
)

# Directory where screenshots will be saved before uploading
screenshot_directory = 'screenshots'
if not os.path.exists(screenshot_directory):
    os.makedirs(screenshot_directory)

def main():
    # Ask the user to input the screenshot interval (in seconds)
    screenshot_interval = float(input("Enter the interval between screenshots (in seconds): "))

    # Initialize the ActivityTracker with the user-defined screenshot interval
    tracker = ActivityTracker(screenshot_interval=screenshot_interval)

    try:
        while True:
            # Track user activity and capture a screenshot
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
