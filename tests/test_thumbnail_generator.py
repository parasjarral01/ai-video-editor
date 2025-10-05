import unittest
from editor.thumbnail_generator import ThumbnailGenerator

class TestThumbnailGenerator(unittest.TestCase):
    def test_generate_thumbnails(self):
        tg = ThumbnailGenerator()
        result = tg.generate_thumbnails("sample_video.mp4")
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()
