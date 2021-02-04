import unittest
from weirdtext.encoder import encode, shuffle_word


class TestEncoder(unittest.TestCase):

    def test_shuffle_short(self):
        """Test checks whether short word will be returned in its original form"""
        input_word = 'abc'
        result = shuffle_word(input_word)
        self.assertEqual(result, input_word)

    def test_shuffle_regular(self):
        """Test checks a regular length word shuffle"""
        input_word = 'test'
        result = shuffle_word(input_word)
        self.assertEqual(result, 'tset')

    def test_shuffle_long_repeated(self):
        """Test checks if word with repeated character in the middle will be returned in its original form"""
        input_word = 'keeeeeeeeeeeey'
        result = shuffle_word(input_word)
        self.assertEqual(result, input_word)

    def test_shuffle_long(self):
        """Test checks if shuffled word is shuffled recpecting the requirements"""
        input_word = 'Mateo'
        possible_permutations = ['Maeto', 'Mtaeo', 'Mteao', 'Metao', 'Meato']
        # Repeat test N times to check different permutations
        for i in range(20):
            result = shuffle_word(input_word)
            self.assertIn(result, possible_permutations)

    def test_encoder(self):
        """Test checks if value returned by encoder is valid"""
        input_text = 'This is my input text'
        result = encode(input_text)
        # Check if encoder returns list of sorted original words
        self.assertEqual(result[1], ['This', 'input', 'is', 'my', 'text'])


if __name__ == '__main__':
    unittest.main()
