import time
import schedule
from activity_tracker import ActivityTracker
from firebase_upload import FirebaseUploader
from config_handler import load_config

def main():
    # Load Firebase credentials
    config = load_config()
    firebase_cred_path = "config/firebase_credentials.json"
    bucket_name = config["project_id"] + ".appspot.com"

    # Initialize modules
    activity_tracker = ActivityTracker(screenshot_interval=60)
    firebase_uploader = FirebaseUploader(firebase_cred_path, bucket_name)

    # Schedule Screenshot Capture and Upload Task
    def capture_and_upload_screenshot():
        screenshot_path = activity_tracker.capture_screenshot()
        firebase_uploader.upload_file(screenshot_path)

    schedule.every(60).seconds.do(capture_and_upload_screenshot)

    # Main loop
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
