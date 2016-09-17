#!/usr/bin/python

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a > b:
        c = b
        while a % c != 0 or b % c != 0:
            c -= 1
    else:
        c = a
        while b % c != 0 or a % c != 0:
            c -= 1
    return c

if __name__ == "__main__":
  print(gcdIter(12, 17))
