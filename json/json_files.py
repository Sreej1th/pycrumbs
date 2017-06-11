#!/usr/bin/env python
from json import load, dump


def read_json(file2read):
    '''Takes a file as argument and returns json read from it'''
    try:
        with open(file2read, 'r') as data_file:
            json_data = load(data_file)
        return json_data
    except Exception as e:
        raise


def write_json(file2write, json2write):
    '''Takes a json and target file and writes data to that file.'''
    try:
        with open(file2write, 'w') as outfile:
            dump(json2write, outfile)
        return True
    except Exception as e:
        raise
