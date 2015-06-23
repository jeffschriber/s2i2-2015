#! /usr/bin/env python

"""
This is a python module that converts temperatures
"""

def f_to_K(temp):
    converted = ((temp - 32) * (5.0 / 9.0)) + 273.15
    return converted

print f_to_K(212)

