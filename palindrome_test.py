import unittest
from palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_example1(self):
        input_string = "race@car#"
        trash_symbols_string = "!@#"
        self.assertTrue(is_palindrome(input_string, trash_symbols_string))

    def test_example2(self):
        input_string = "RaCeaCcaA@r$#!"
        trash_symbols_string = "!@#$"
        self.assertFalse(is_palindrome(input_string, trash_symbols_string))

    def test_example3(self):
        input_string = "a@b!!b$a"
        trash_symbols_string = "!@#$"
        self.assertTrue(is_palindrome(input_string, trash_symbols_string))

    def test_example4(self):
        input_string = "?Aa#c"
        trash_symbols_string = "#?"
        self.assertFalse(is_palindrome(input_string, trash_symbols_string))

    def test_example5(self):
        input_string = "!M@alay@alam!"
        trash_symbols_string = "!@"
        self.assertTrue(is_palindrome(input_string, trash_symbols_string))

    def test_example6(self):
        input_string = "a!B@A#*"
        trash_symbols_string = "!@#*"
        self.assertTrue(is_palindrome(input_string, trash_symbols_string))

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
