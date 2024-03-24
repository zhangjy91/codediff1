import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')

    def test_lower(self):
        self.assertEqual('DVD'.lower(),'dvd')

    def test_check(self):
        self.assertTrue('SET'.isupper())


if __name__ == '__main__':
    unittest.main()
