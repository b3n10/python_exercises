#!/usr/bin/python3

import args

def maxi(args1, args2=0):
 if args1 > args2:
  return args1
  print('{0} is greater than {1}'.format(args1, args2))
 else:
  return args2
  print('{1} is greater than {0}'.format(args1, args2))

if __name__ == '__main__':
 if args.main(2) != None:
  num1, num2 = args.main(2)
  print(type(num1), ' ', type(num2))
  print( maxi(num1, num2) )
 else:
  print("More than 2 values entered. Only need 2.")
