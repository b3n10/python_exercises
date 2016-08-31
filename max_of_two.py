#!/usr/bin/python3

import args

def main(args1, args2=0):
 if args1 > args2:
  return args1
 else:
  return args2

if __name__ == '__main__':
 if args.main(2) != None:
  num1, num2 = args.main(2)
  print( main(num1, num2) )
 else:
  print("More than 2 values entered. Only need 2.")
