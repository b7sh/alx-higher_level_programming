#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """the test cases"""
    

    def test_ord_list(self):
        """test the orderd list"""
        order = [1, 2, 3, 4]
        self.assertEqual(max_integer(order), 4)


    def test_unord_list(self):
        """test unorderd list"""
        unord = [1, 2, 3, 4]
        self.assertEqual(max_integer(unord,), 4)


    def test_max_at_begin(self):
        """test the bigining max value"""
        max_at_begin = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_begin), 4)


    def test_empt(self):
        """test if the list is empty"""
        emp = []
        self.assertEqual(max_integer(emp), None)


    def test_element(self):
        """test one of the elements"""
        ele = [7]
        self.assertEqual(max_integer(ele), 7)


    def test_float(self):
        """test the float list"""
        float_list = [1.45, -7.57, 8.78, 6.26, 4.0]
        self.assertEqual(max_integer(float_list), 8.78)


    def test_int_nd_float(self):
        """test the float and integer list"""
        int_nd_float = [3.33, 21, 9.6, 6, 2.7]
        self.assertEqual(max_integer(int_nd_float), 21)


    def test_str(self):
        """test the string"""
        string = "Boshy"
        self.assertEqual(max_integer(string), 'y')


    def test_str_list(self):
        """test the string list"""
        string_list = ["I", "love", "my", "brothers"]
        self.assertEqual(max_integer(string_list), 'my')


    def test_emp_str(self):
        """test an empty string"""
        self.assertEqual(max_integer(""), None)


    if __name__ == '__main__':
        unittest.main()
