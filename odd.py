#!/usr/bin/python

def main(x, y, z):
    if x % 2 != 0 or y % 2 != 0 or z % 2 != 0:
        if x > y and x > z and x % 2 != 0:
            print("Largest odd is: " + str(x))
        elif y > x and y > z and y % 2 != 0:
            print("Largest odd is: " + str(y))
        elif z % 2 != 0:
            print("Largest odd is: " + str(z))
    else:
        print("No numbers are odd.")

main(11, 10, 15)
