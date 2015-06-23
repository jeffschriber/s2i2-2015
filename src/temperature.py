#! /usr/bin/env python

"""
This is a python module that converts temperatures
"""

def f_to_K(temp):
    converted = ((temp - 32) * (5.0 / 9.0)) + 273.15
    return converted

def K_to_C(temp):
    return temp - 273.15

def f_to_C(temp):
    return K_to_C(f_to_K(temp))


print K_to_C(273.15)
print f_to_C(32)

