import unittest
from editor.metadata_generator import MetadataGenerator

class TestMetadataGenerator(unittest.TestCase):
    def test_generate_metadata(self):
        mg = MetadataGenerator()
        result = mg.generate_metadata("sample transcript")
        self.assertIn("title", result)
        self.assertIn("description", result)

if __name__ == '__main__':
    unittest.main()
