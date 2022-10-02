#!/usr/bin/env python3

"""
Tests the method Check email
"""
import unittest
import sys
from utils import check_phone


__author__ = 'Anton Maynard'
__version__ = 'Fall 2022'
__pylint__ = '1.8.3.'


class TestValidate(unittest.TestCase):
    
    def test_valid_phone(self):
        """
        Tests the method Check phone with no dashes or brackets
        """
        self.assertTrue(check_phone("1234567890"))
    
    def test_valid_phone_with_dashes(self):
        """
        Tests the method Check phone with dashes
        """
        self.assertTrue(check_phone("123-456-7890"))
        
    def test_valid_phone_with_brackets(self):
        """
        Tests the method Check phone with brackets and dashes
        """
        self.assertTrue(check_phone("(123)456-7890"))
        
    def test_valid_phone_with_plus(self):
        """
        Tests the method Check phone with plus sign
        """
        self.assertTrue(check_phone("+1234567890"))
    
    def test_invalid_phone_Length(self):
        """
        Tests the method Check phone with invalid phone number length
        """
        self.assertFalse(check_phone("123456789"))
    
        
    
if __name__ == '__main__':
    unittest.main()