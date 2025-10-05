class ThumbnailGenerator:
    def generate_thumbnails(self, video_path: str):
        thumbnails = []
        for i in range(3):
            thumbnails.append(f"thumbnail_{i}.jpg")
        return thumbnails
