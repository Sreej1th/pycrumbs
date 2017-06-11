#!/usr/bin/env python
from os import remove, stat
from shutil import copyfile


def write_file(file_data, out_file):
    '''Takes a file and data as args, writes data and reverts on fail.'''
    try:
        if stat(out_file):
            copyfile(out_file, 'temp_file_bak')
        with open(out_file, 'w') as outfile:
            outfile.write(file_data)
    except Exception as e:
        copyfile('temp_file_bak', out_file)
    finally:
        remove('temp_file_bak')


def read_file(in_file):
    '''Takes file as args and read line by line and return data as list.'''
    try:
        with open(in_file, 'r') as infile:
            file_data = infile.readlines()
        return [lines.strip() for lines in file_data]
    except IOError:
        print ('File %s does not exit or permission denied.') % (in_file)
    except Exception as e:
        raise
