from .file_handler import FileHandler

class TextHandler(FileHandler):
    def __init__(self, upload_dir):
        super().__init__(upload_dir)

    def save_text(self, file, filename):
        # Add any text-specific handling here
        self.save_file(file, filename)