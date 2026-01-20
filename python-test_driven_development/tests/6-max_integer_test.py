#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
import sys
import os

# Ajouter la racine du projet dans sys.path pour que Python trouve '6-max_integer.py'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test list with max at beginning"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test list with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test list with integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)


if __name__ == '__main__':
    unittest.main()
