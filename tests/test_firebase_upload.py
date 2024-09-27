import unittest
from unittest import mock
from firebase_upload import FirebaseUploader

class TestFirebaseUploader(unittest.TestCase):

    @mock.patch('firebase_upload.storage')
    def test_upload_file(self, mock_storage):
        # Set up mock bucket and blob
        mock_bucket = mock_storage.bucket.return_value
        mock_blob = mock_bucket.blob.return_value
        
        # Initialize FirebaseUploader with mock credentials
        uploader = FirebaseUploader(cred_path="tests/mock_firebase_credentials.json", bucket_name="mock-bucket")
        
        # Call the upload function
        uploader.upload_file("tests/mock_file.png")

        # Assert that the blob.upload_from_filename was called with correct file path
        mock_blob.upload_from_filename.assert_called_with("tests/mock_file.png")

if __name__ == "__main__":
    unittest.main()
