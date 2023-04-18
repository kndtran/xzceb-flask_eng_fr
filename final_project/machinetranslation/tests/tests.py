import unittest
import pytest

from translator import english_to_french, french_to_english


class TestStringMethods(unittest.TestCase):

    def test_e2f_null(self):
        text = None
        with pytest.raises(ValueError):
            translated = english_to_french(text)

    def test_f2e_null(self):
        text = None
        with pytest.raises(ValueError):
            translated = french_to_english(text)

    def test_e2f(self):
        text = "Hello"
        translated = english_to_french(text)
        expected = "Bonjour"
        self.assertEqual(translated["translations"][0]["translation"], expected)

    def test_f2e(self):
        text = "Bonjour"
        translated = french_to_english(text)
        expected = "Hello"
        self.assertEqual(translated["translations"][0]["translation"], expected)


if __name__ == '__main__':
    unittest.main()
