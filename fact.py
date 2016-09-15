#!/usr/bin/python3

def main(x):
    """
    Takes input from user
    Returns factorial of input
    This is a sample from edX.org "MITx: 6.00.1x Introduction to Computer Science and Programming Using Python"
    """
    if x == 1:
        return 1
    else:
        return x * main(x-1)

if __name__ == "__main__":
    x = int(input("Enter a number: "))
    print("The factorial of " + str(x) + " is " +  str(main(x)))
