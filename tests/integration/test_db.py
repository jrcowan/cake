import unittest


class MyTestCase(unittest.TestCase):
    def test_sqlite(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
