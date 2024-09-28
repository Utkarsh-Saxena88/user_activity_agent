import pyautogui
import time
import random
from datetime import datetime
import os

class ActivityTracker:
    def __init__(self, screenshot_interval=5, suspicious_thresholds=None):
        self.last_mouse_position = pyautogui.position()
        self.last_mouse_time = time.time()
        self.last_keystroke_time = time.time()
        self.suspicious_flag = False
        self.screenshot_interval = screenshot_interval  # Add screenshot interval
        self.suspicious_thresholds = suspicious_thresholds or {
            'max_speed': 3000,  # Maximum pixels per second for mouse movement
            'min_randomness': 0.1,  # Minimum randomness in movement trajectory
            'keystroke_min_interval': 0.05,  # Minimum interval between keystrokes in seconds
        }

    def capture_screenshot(self, suspicious=False):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        if suspicious:
            filename = f"SuspiciousActivity_{timestamp}.png"
        else:
            filename = f"UserActivity_{timestamp}.png"
        filepath = os.path.join('screenshots', filename)
        
        # Capture and save screenshot
        screenshot = pyautogui.screenshot()
        screenshot.save(filepath)
        return filepath  # Return the path to the screenshot

    def monitor_mouse_movement(self):
        current_mouse_position = pyautogui.position()
        current_time = time.time()

        # Calculate speed of mouse movement
        distance = ((current_mouse_position[0] - self.last_mouse_position[0]) ** 2 +
                    (current_mouse_position[1] - self.last_mouse_position[1]) ** 2) ** 0.5
        time_diff = current_time - self.last_mouse_time
        speed = distance / time_diff if time_diff > 0 else 0

        # Analyze movement randomness
        randomness = random.random()  # Simulate randomness for now, can be enhanced

        # Flagging suspicious activity based on speed and randomness
        if speed > self.suspicious_thresholds['max_speed'] or randomness < self.suspicious_thresholds['min_randomness']:
            self.suspicious_flag = True
            print("Suspicious mouse activity detected")
        else:
            self.suspicious_flag = False
            print("Normal User mouse activity detected")

        self.last_mouse_position = current_mouse_position
        self.last_mouse_time = current_time

    def monitor_keystrokes(self):
        current_time = time.time()
        keystroke_interval = current_time - self.last_keystroke_time

        # Check for rapid, constant keystrokes
        if keystroke_interval < self.suspicious_thresholds['keystroke_min_interval']:
            self.suspicious_flag = True
            print("Suspicious keystroke activity detected")
        else:
            self.suspicious_flag = False
            print("Normal User keystroke activity detected")

        self.last_keystroke_time = current_time

    def track_user_activity(self):
        self.monitor_mouse_movement()
        self.monitor_keystrokes()

        # Take a screenshot and return the path to the screenshot
        if self.suspicious_flag:
            return self.capture_screenshot(suspicious=True)
        else:
            return self.capture_screenshot(suspicious=False)
