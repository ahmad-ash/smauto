from instagrapi import Client
import os
import time

class InstagramUploader:
    def __init__(self, username, password):
        self.client = Client()
        self.session_file = "session.json"

        # Load session if it exists
        if os.path.exists(self.session_file):
            try:
                self.client.load_settings(self.session_file)
                self.client.login(username, password)
                print("Instagram session loaded successfully!")
            except Exception as e:
                print(f"Error loading session: {e}")
                self._login(username, password)
        else:
            self._login(username, password)

    def _login(self, username, password):
        """
        Logs in to Instagram and saves the session.
        """
        try:
            self.client.login(username, password)
            self.client.dump_settings(self.session_file)
            print("Logged in to Instagram and session saved!")
        except Exception as e:
            print(f"Error logging in to Instagram: {e}")
            raise

    def upload_video(self, video_path, caption):
        """
        Uploads a video to Instagram with the given caption.
        """
        try:
            self.client.clip_upload(video_path, caption=caption)
            print("Video uploaded successfully!")
        except Exception as e:
            print(f"Error uploading video: {e}")
            raise