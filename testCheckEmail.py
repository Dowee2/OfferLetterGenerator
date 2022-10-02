#!/usr/bin/env python3

"""
Tests the method Check email
"""
import unittest

from utils import check_email


__author__ = 'Anton Maynard'
__version__ = 'Fall 2022'
__pylint__ = '1.8.3.'


class TestValidate(unittest.TestCase):
    """
    Tests the method Check email
    """
    def test_check_Valid_email(self):
        """
        Tests the method Check email with a valid email
        """
        self.assertTrue(check_email("Anton.Maynard@gmail.com"))
        
    def test_valid_email_no_periods(self):
        """
        Tests the method Check email no periods in email
        """
        self.assertTrue(check_email("amaynar2@gmail.com"))
    
    def test_no_top_level_domain(self):
        """
        Tests the method Check email with no top level domain
        """
        self.assertFalse(check_email("Anton.Maynard@Gmail"))
    
    def test_check_invalid_email(self):
        """
        Tests the method Check email with no top level domain but period
        """
        self.assertFalse(check_email("Anton.Maynard@Gmail."))
        
    def test_check_invalid_email_no_at(self):
        """
        Tests the method Check email with no @
        """
        self.assertFalse(check_email("Anton.MaynardGmail.com"))
         
if __name__ == '__main__':
    unittest.main()
