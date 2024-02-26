from .file_handler import FileHandler

class VideoHandler(FileHandler):
    def __init__(self, upload_dir):
        super().__init__(upload_dir)

    def save_video(self, file, filename):
        # Add any video-specific handling here
        self.save_file(file, filename)