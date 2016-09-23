def main(char, myString):
    '''
    char: a single character
    myString: an alphabetized string
    returns: True if char is in myString; False otherwise
    '''
    # Your code here
    # abcdEfghI
    x = int(len(myString)/2)    

    if x == 0:
        return False
    else:
        testChar = myString[x]
        if char == testChar:
            return True
        elif char < testChar:
            return main(char, myString[:x])
        elif char > testChar:
            return main(char, myString[x:])

if __name__ == "__main__":
    print( main('g', 'cdghmoqrsvyy') )
