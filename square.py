#!/usr/bin/python3

'''
Created on Sept 15, 2016
Author: Francis Ben Lleve
'''

def main():
    """
    Takes input from user
    Returns the square of the input
    """
    x = int( input("Enter any number: ") )

    return "The square of " + str(x) + " is " + str(x**2)

if __name__ == "__main__":
    print(main())
