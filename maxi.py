#!/usr/bin/python3

import args

def maxi(args1, args2=0):
 if args1 > args2:
  return args1
 else:
  return args2

if __name__ == '__main__':
 num1, num2 = args.main()
 print( maxi(num1, num2) )
