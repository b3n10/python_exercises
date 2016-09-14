#!/usr/bin/python3

'''
Created on Sep 12, 2016 at 5:09AM

Author: Francis Ben Lleve
'''
def main():
    """
    Prints guessed number, accepts input as h 'high',l 'low', 'c' correct
    """
    i, g, s, e = '', 50, 0, 100

    while i != 'c':
        #print('g: {0}, s: {1}, e: {2}'.format(str(g),str(s),str(e)))
        print('Is your secret number ' + str(g) + '?')
        i = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        if i == 'h':
            e = g
            if e - s <= 5:
                g = int(g - 1)
            else:
                g = s + int((e - s) / 2)
                #e = int(g)
        elif i == 'l':  
            s = g
            if e - s <= 2:
                g = int(g + 1)
            else:
                g += int((e - s) / 2)
        elif i == 'c':
            print('I have guessed it correctly: ' + str(g))
        else:
            print('Incorrect input')

if __name__ == '__main__':
    main()
