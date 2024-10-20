import unittest
from MykytaWord import WordCounter

class TestWordCounter(unittest.TestCase):
    def setUp(self):
        self.counter = WordCounter()

    def test_count_words_empty_string(self):
        self.assertEqual(self.counter.count(""), 0)

    def test_count_words_single_word(self):
        self.assertEqual(self.counter.count("hello"), 1)

    def test_count_words_multiple_words(self):
        self.assertEqual(self.counter.count("hello world"), 2)

    def test_count_words_with_extra_spaces(self):
        self.assertEqual(self.counter.count("  hello   world  "), 2)

    def test_count_words_special_characters(self):
        self.assertEqual(self.counter.count("hello, world!"), 2)

if __name__ == "__main__":
    unittest.main()