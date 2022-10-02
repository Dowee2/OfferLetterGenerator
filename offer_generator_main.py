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
    if(len(filenames) == 3):
        print(filenames)
        read_from_disk(filenames)
    elif(len(filenames) == 1):
        template = input("Please provide the location to the offer letter template: ")
        filenames.insert(1,template)
        candidate_list = input("Please provide the location to the candidate list: ")
        filenames.insert(2,candidate_list)
        print(filenames)
        read_from_disk(filenames)
    else:
        input("Please rerun this program with the correct number of arguments i.e offer_generator_main.py <template> <candidate_list>")
        return
    
    

if __name__ == '__main__':
    main(sys.argv)
