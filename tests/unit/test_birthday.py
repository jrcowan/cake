import io
import sys
import unittest
from unittest import TestCase
from unittest.mock import patch
from src.birthday import *


class Test(TestCase):

    @patch('builtins.input', return_value='12/12/2012')
    def test_get_birthday_value(self, mock_input):
        result = get_birthday_value()
        test_date = date(2012, 12, 12)
        self.assertEqual(result, test_date)


if __name__ == '__main__':
    unittest.main()
