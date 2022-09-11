import unittest
from .translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_french_to_english(self):
        self.assertIsNone(french_to_english(None),'Input is null')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_english_to_french(self):
        self.assertIsNone(english_to_french(None),'Input is null')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()