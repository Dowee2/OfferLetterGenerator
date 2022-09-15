#!/usr/bin/env python3
"""
Lecture 5 - File IO.
"""

import sys
import lib5

__author__ = 'CS3280'
__version__ = 'Fall 2021'
__pylint__ = '1.8.3.'


def read_from_disk(filename):
    """
    Reads content of file.
    Args: - filename the name of the file
    """
    try:
        with open(filename) as input_file:
            #content = input_file.read()
            #print(content)
            list_of_lines = input_file.readlines()
            print(list_of_lines[0])

        print('File is closed?', input_file.closed)
    except IOError as error:
        print('Problem:', error)

def write_to_disk(filename):
    """
    Writes content to file.
    Args: - filename the name of the file
    """
    try:
        with open(filename, 'w') as output_file:
            output_file.write('Hello from script!\n')
    except IOError as error:
        print('Problem:', error)

def main(parameter):
    """
    Main entry point.
    """
    #read_from_disk(parameter)
    #write_to_disk(parameter)
    print(lib5.is_valid_uwg_id(parameter))

if __name__ == '__main__':
    main(sys.argv[1])
