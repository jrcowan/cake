import unittest

from src.main import get_data


class TestData(unittest.TestCase):
    def test_get_data(self):
        self.assertEqual(get_data('test'), 'test')  # add assertion here


if __name__ == '__main__':
    unittest.main()
