"""
Tests for the translator file
"""

import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """
    Class that unit test the translator
    """
    def test_english_to_french(self):
        """
        Test for french translation
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english(self):
        """
        Test for english translation
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == "__main__":
    unittest.main()
