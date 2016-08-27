#/usr/bin/python

import sys

def main():
 argv = []
 argv[:] = [ int(x) for x in sys.argv[1:] ]
 num1, num2 = argv[:2]
 return num1, num2

if __name__ == "__main__":
 main()

