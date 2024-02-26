from .file_handler import FileHandler

class ImageHandler(FileHandler):
    def __init__(self, upload_dir):
        super().__init__(upload_dir)

    def save_image(self, file, filename):
        # Add any image-specific handling here
        self.save_file(file, filename)