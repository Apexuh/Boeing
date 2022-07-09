import unittest

from Boeing import Boeing737


class TestUpper(unittest.TestCase):
    boeing = Boeing737()

    def test_request_with_all_wishes_1(self):
        """With 3 args (2 left aisle)"""
        self.assertEqual(self.boeing.request_with_all_wishes('2 left aisle'), {'count_of_buyers': 2, 'side': 'left', 'place': 'aisle'})

    def test_request_with_all_wishes_2(self):
        """With 3 args (window left 3)"""
        self.assertEqual(self.boeing.request_with_all_wishes('window left 3'), {'count_of_buyers': 3, 'side': 'left', 'place': 'window'})

    def test_request_with_all_wishes_3(self):
        """With 2 args (2 right)"""
        self.assertEqual(self.boeing.request_with_all_wishes('2 right'), {'count_of_buyers': 2, 'side': 'right'})

    def test_request_with_all_wishes_4(self):
        """With 2 args (2 aisle)"""
        self.assertEqual(self.boeing.request_with_all_wishes('2 aisle'), {'count_of_buyers': 2, 'place': 'aisle'})

    def test_request_with_all_wishes_5(self):
        """With 1 arg (6)"""
        self.assertEqual(self.boeing.request_with_all_wishes('6'), {'count_of_buyers': 6})

    def test_request_with_all_wishes_6(self):
        """With 1 arg (7)"""
        self.assertEqual(self.boeing.request_with_all_wishes('7'), 'Please input correct information')

    def test_request_with_all_wishes_7(self):
        """With 1 arg (-7)"""
        self.assertEqual(self.boeing.request_with_all_wishes('-7'), 'Please input correct information')

    def test_request_with_all_wishes_8(self):
        """With no args"""
        self.assertEqual(self.boeing.request_with_all_wishes(''), 'Please input correct information')

if __name__ == '__main__':
    unittest.main()