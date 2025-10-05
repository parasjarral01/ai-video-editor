import unittest
from editor.translator import Translator

class TestTranslator(unittest.TestCase):
    def test_translate_text(self):
        tr = Translator()
        text = "Hello world"
        translated = tr.translate_text(text, "es")
        self.assertTrue(translated.startswith("[Translated es]"))

if __name__ == '__main__':
    unittest.main()
