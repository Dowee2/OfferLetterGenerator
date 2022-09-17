#!/usr/bin/env python3
"""
A Offer Letter Generator
"""

import sys

import offer_letter_generator


__author__ = 'Anton Maynard'
__version__ = 'Fall 2022'
__pylint__ = '1.8.3.'


def read_from_disk(filename):
    """
    Reads content of file.
    Args: - filename the name of the file
    """
    try:
        with open(filename[1], 'r') as input_file:
            with open(filename[2], 'r') as input_file2:
                generate = offer_letter_generator.OfferGenerator()
                content = input_file.read()
                input_file.seek(0,0)
                print(content)
                if content.__contains__("Candidate List"):
                    generate.parse_candidates_from_file(input_file2.read(),input_file.readlines())
                else:
                    generate.parse_candidates_from_file(content, input_file2.readlines())
                    

    except IOError as error:
        print('Problem:', error)
        input()
def main(filenames):
    """
    Main entry point.
    """
    read_from_disk(filenames)
    

if __name__ == '__main__':
    main(sys.argv)
