import unittest
from editor.export_system import ExportSystem

class TestExportSystem(unittest.TestCase):
    def test_export_video(self):
        es = ExportSystem()
        path = es.export_video("sample_video.mp4", save_path="./output_test")
        self.assertTrue(path.endswith(".mp4"))

if __name__ == '__main__':
    unittest.main()
