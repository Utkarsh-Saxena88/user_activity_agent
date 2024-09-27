import unittest
import os
from activity_tracker import ActivityTracker

class TestActivityTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = ActivityTracker()

    def test_capture_screenshot(self):
        # Test screenshot capture functionality
        screenshot_path = self.tracker.capture_screenshot()
        self.assertTrue(os.path.exists(screenshot_path))
        
        # Clean up created screenshot
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)

    def test_active_window_tracking(self):
        # Test that active window tracking returns a valid string (dummy process name)
        process_name = self.tracker.track_active_window()
        self.assertIsInstance(process_name, str)

if __name__ == "__main__":
    unittest.main()
