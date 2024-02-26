import os

class FileHandler:
    def __init__(self, upload_dir):
        self.upload_dir = upload_dir

    def save_file(self, file, filename):
        file.save(os.path.join(self.upload_dir, filename))