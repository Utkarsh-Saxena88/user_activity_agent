from pynput import keyboard, mouse
import pyautogui
import psutil
from datetime import datetime

class ActivityTracker:
    def __init__(self, screenshot_interval=60):
        self.screenshot_interval = screenshot_interval

    def capture_screenshot(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"screenshots/screenshot_{timestamp}.png"
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        print(screenshot_path)
        return screenshot_path

    def monitor_keyboard(self):
        def on_press(key):
            print(f"Key {key} pressed")

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def monitor_mouse(self):
        def on_click(x, y, button, pressed):
            print(f"Mouse clicked at {(x, y)} with {button}")

        with mouse.Listener(on_click=on_click) as listener:
            listener.join()

    def track_active_window(self):
        current_process = psutil.Process(psutil.Process().ppid())
        return current_process.name()
