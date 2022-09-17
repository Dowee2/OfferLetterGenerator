#!/usr/bin/env python3

"""
Utilities for Letter Generator
"""

import re
# Please run the command pip install fpdf to allow this to work
from fpdf import FPDF

__author__ = 'Anton Maynard'
__version__ = 'Fall 2022'
__pylint__ = '1.8.3.'


def generate_pdf(content, file_name):
    pdf_creator = FPDF()
    pdf_creator.add_page()
    pdf_creator.set_font("Arial", size=13)
    pdf_creator.multi_cell(0, 10, txt=content, align='l')
    pdf_creator.output(f'offers/{file_name}.pdf')
    


def check_email(email: str) -> bool:
    '''
    This is a regex for email validation
    '''
    regex = re.compile(r'[A-Z a-z 0-9]*\.?_?[A-Z a-z 0-9]*@[A-Z a-z]*\.[A-Z a-z]{2,}')
    return regex.search(email) is not  None



def check_phone(phone: str) -> bool:
    '''
    This is a regex for phone number validation
    '''
    regex = re.compile(r'[0-9]{10,12}')
    phone = phone.replace("-", "")
    phone = phone.replace("(", "")
    phone = phone.replace(")", "")
    phone = phone.replace("+", "")
    phone = phone.replace(" ", "")
    
    return regex.search(phone) is not None
