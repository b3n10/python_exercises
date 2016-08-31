#!/usr/bin/python3

import args

def main(args1, args2=0, args3=0):
 if args1 > args2 and args1 > args3:
  return args1
 elif args2 > args1 and args2 > args3:
  return args2
 else:
  return args3

if __name__ == '__main__':
 if args.main(3) != None:
  num1, num2, num3 = args.main(3)
  print( main(num1, num2, num3) )
 else:
  print("More than 3 values entered. Only need 2.")
