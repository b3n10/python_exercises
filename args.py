#/usr/bin/python

import sys

def main(args):
# argv = []
 x = args + 1

 if not len(sys.argv) > x:
  d = {}
  for a in sys.argv[1:x]:
   d['{0}'.format(a)] = int(a)
  #print( d.values() )
  return d.values()
# argv[:] = [ int(x) for x in sys.argv[1:] ]
# num1, num2 = argv[:2]
# return num1, num2

if __name__ == "__main__":
 main(0)
