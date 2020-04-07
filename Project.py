from pathlib import Path

class Project():
    def __init__(self):
        self.name = "transfer-learning-image-art"
        self.base_dir = Path(__file__).parent
        content_filename = ""
        style_filename = ""
        self.content_img_path = self.base_dir / "images" / content_filename
        self.style_img_path = self.base_dir / "images" / style_filename