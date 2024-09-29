
# Activity Tracker Application

## Description
The **Activity Tracker Application** is a Python-based tool designed to monitor and log user activities on a system. It automates the process of recording activities and can upload the data to Firebase for secure storage and further processing. With features like real-time tracking and automated uploads, this application serves as a robust solution for activity tracking in various scenarios such as productivity monitoring, security logging, and time management.

## Features
- **Activity Tracking**: Monitors and records user activity data.
- **Firebase Integration**: Uploads tracked data to Firebase for centralized storage.
- **Real-time Monitoring**: Logs activities in real-time using efficient background processes.
- **Automation**: Operates silently in the background, automatically logging and uploading data.

## Installation

### Prerequisites
- Python 3.x
- Firebase project with access credentials
- Required libraries (specified in `requirements.txt`)

### Steps
1. Clone the repository:
    git clone https://github.com/yourusername/activity-tracker.git
    cd activity-tracker

2. Install the required dependencies:
    pip install -r requirements.txt

3. Set up Firebase:
   - Download your Firebase Admin SDK credentials (`serviceAccountKey.json`).
   - Place the credentials file in the project directory.
   - Update the Firebase configuration in `firebase_upload.py`.

4. Run the application:
    python main.py

## Usage

1. **Track Activity**: The application automatically tracks user activities (e.g., key presses, screen usage).
2. **Upload to Firebase**: Activity logs are uploaded to Firebase in real-time.
3. **Monitor and Analyze**: Use Firebase to review the data and generate reports or visualizations for analysis.

### Example Commands:
python activity_tracker.py  # Starts tracking user activity
python firebase_upload.py    # Manually uploads data to Firebase
python main.py               # Main script to run both tracking and upload functionalities

## Configuration
- Modify `firebase_upload.py` to change Firebase storage paths or adjust how data is structured.
- `activity_tracker.py` contains logic for tracking activities; adjust intervals, formats, or specific events to track.

## File Structure
.
├── activity_tracker.py      # Handles user activity tracking
├── firebase_upload.py       # Manages Firebase upload functionality
├── main.py                  # Main entry point to run the application
├── requirements.txt         # Dependencies for the project
└── README.md                # Project documentation

## Requirements

The following Python packages are required:
- Pillow
- cryptography
- filelock
- firebase-admin
- google-api-python-client
- pyautogui
- pytz
- requests

Install all dependencies via:
pip install -r requirements.txt

## Contributors
- Utkarsh-Saxena88 - Initial development

Feel free to contribute to this project by opening issues or submitting pull requests.

