#!/usr/bin/python3
'''
This is part of edX's Intro to CS w/ Python
url: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2016
'''

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0 
    returns: int or float, base^exp
    '''
    if exp > 0:
        if exp == 0:
            return 1
        else:
            return base * recurPower(base, exp - 1)
    else:
        return 1

if __name__ == "__main__":
    print(recurPower(-4.44, 5))
