import unittest
from weirdtext.decoder import decode, decode_word, check_input_validity


class TestDecoder(unittest.TestCase):

    def test_decode_word(self):
        """Test checks if value returned by encoder is valid"""
        encoded_word = 'tihs'
        decode_possibilities = ['is', 'this', 'Sparta']
        result = decode_word(encoded_word, decode_possibilities)
        self.assertEqual(result, 'this')

    def test_validator(self):
        """Test checks if validator raises exception when there are no proper words to refer"""
        weirdtext = '\n--weird--\n' + 'That isn\'t going to happen' + '\n--weird--\n'
        decode_possibilities = ['is', 'this', 'Sparta']
        decode_possibilities.sort()
        self.assertRaises(ValueError, check_input_validity, weirdtext, decode_possibilities)

    def test_separator_missing(self):
        """Test checks validation function when the magic separator is missing in the text"""
        weirdtext = "tihs is Sprata"
        decode_possibilities = ['is', 'this', 'Sparta']
        decode_possibilities.sort()
        self.assertRaises(ValueError, check_input_validity, weirdtext, decode_possibilities)

    def test_decode(self):
        """Test checks decode function"""
        weirdtext = '\n--weird--\n' + 'Tihs is Bldaangseh' + '\n--weird--\n'
        original_words = ['Bangladesh', 'This', 'is']
        expected_text = "This is Bangladesh"
        result = decode(weirdtext, original_words)
        self.assertEqual(result, expected_text)


if __name__ == '__main__':
    unittest.main()
