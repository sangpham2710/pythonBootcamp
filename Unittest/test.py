import unittest
import main


class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = main.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = "hi i am using python"
        result = main.cap_text(text)
        self.assertEqual(result, "Hi I Am Using Python")


if __name__ == '__main__':
    unittest.main()
