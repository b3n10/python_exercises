#!/usr/bin/python3

import sys

def maxi(args1, args2=0):
 if args1 > args2:
  return args1
 else:
  return args2

if __name__ == '__main__':
 argv = [] 
 argv[:] = [ int(x) for x in sys.argv[1:] ] 
 num1, num2 = argv[:2]
 print( maxi(num1, num2) )
