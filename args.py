#/usr/bin/python

import sys

def main(args):
 x = args + 1

 if len(sys.argv) == 1:
  return None
 elif len(sys.argv) == x or len(sys.argv) < x:
  d = {}
  for a in sys.argv[1:x]:
   d['{0}'.format(a)] = int(a)
  #print( d.values() )
  return d.values()

if __name__ == "__main__":
 main(0)
