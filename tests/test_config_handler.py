import unittest
from config_handler import load_config

class TestConfigHandler(unittest.TestCase):

    def test_load_config(self):
        # Assuming config/firebase_credentials.json exists and is valid
        config = load_config("tests/mock_firebase_credentials.json")
        
        # Check that the loaded config is a dictionary and contains necessary keys
        self.assertIsInstance(config, dict)
        self.assertIn("type", config)
        self.assertIn("project_id", config)
        self.assertIn("private_key_id", config)

if __name__ == "__main__":
    unittest.main()
