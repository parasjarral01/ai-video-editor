import unittest
from editor.editing_panel import EditingPanel

class TestEditingPanel(unittest.TestCase):
    def setUp(self):
        self.editor = EditingPanel()

    def test_color_grading(self):
        self.assertIsNone(self.editor.color_grading("sample_video.mp4"))

    def test_speed_control(self):
        self.assertIsNone(self.editor.speed_control("sample_video.mp4", speed_factor=2.0))

if __name__ == '__main__':
    unittest.main()
