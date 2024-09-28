import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firestore
cred = credentials.Certificate('config/db-firebase-credentials.json')  # Update with your credentials path
firebase_admin.initialize_app(cred)

db = firestore.client()
