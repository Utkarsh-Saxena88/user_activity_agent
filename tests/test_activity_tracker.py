
import unittest
from unittest.mock import patch, MagicMock
import time
import pyautogui
import os
from activity_tracker import ActivityTracker
from firebase_upload import FirebaseUploader
from PIL import Image

class TestActivityTracker(unittest.TestCase):
    @patch('pyautogui.screenshot')
    @patch('activity_tracker.ActivityTracker.load_config')
    @patch('pyautogui.position', return_value=(100, 100))
    @patch('time.time', return_value=1000)
    def test_track_user_activity(self, mock_time, mock_position, mock_screenshot, mock_load_config):
        mock_load_config.return_value = None
        
        # Create a mock image object to return from pyautogui.screenshot
        mock_image = MagicMock(spec=Image.Image)
        mock_image.convert.return_value = mock_image  # Mock the convert method
        
        mock_screenshot.return_value = mock_image
        
        # Create an instance of the uploader mock
        mock_uploader = MagicMock(FirebaseUploader)
        tracker = ActivityTracker(uploader=mock_uploader)
        
        # Track the user activity
        screenshot_path = tracker.track_user_activity()
        
        # Check that a screenshot is returned (since capture_enabled is True by default)
        self.assertTrue(screenshot_path.endswith('.png'), f"Screenshot path: {screenshot_path}")
    
    @patch('activity_tracker.ActivityTracker.detect_timezone', return_value="UTC")
    def test_time_zone_change(self, mock_timezone):
        # Create an instance of the uploader mock
        mock_uploader = MagicMock(FirebaseUploader)
        tracker = ActivityTracker(uploader=mock_uploader)
        
        # Simulate time zone change
        tracker.current_timezone = "PST"
        tracker.check_time_zone_change()
        
        # Verify that the time zone is updated
        self.assertEqual(tracker.current_timezone, "UTC")

    @patch('firebase_upload.FirebaseUploader.upload_file')
    def test_file_upload_success(self, mock_upload):
        # Mock successful file upload
        mock_upload.return_value = True
        uploader = FirebaseUploader(cred_path="dummy_path", bucket_name="dummy_bucket", password="dummy_password")
        
        result = uploader.upload_file('dummy_file.png')
        self.assertTrue(result)

    @patch('firebase_upload.FirebaseUploader.upload_file')
    def test_file_upload_failure(self, mock_upload):
        # Mock failed file upload
        mock_upload.side_effect = Exception("Network error")
        uploader = FirebaseUploader(cred_path="dummy_path", bucket_name="dummy_bucket", password="dummy_password")
        
        with self.assertRaises(Exception) as context:
            uploader.upload_file('dummy_file.png')
        
        self.assertTrue("Network error" in str(context.exception))

    @patch('activity_tracker.ActivityTracker.track_user_activity')
    def test_screenshot_interval(self, mock_track):
        # Ensure screenshots are taken at the right intervals
        mock_uploader = MagicMock(FirebaseUploader)
        tracker = ActivityTracker(uploader=mock_uploader, screenshot_interval=2)
        
        mock_track.return_value = 'dummy_path.png'
        tracker.track_user_activity()
        
        time.sleep(2)  # Simulate waiting for 2 seconds
        mock_track.assert_called()

if __name__ == '__main__':
    unittest.main()
