#!/usr/bin/python

def main(s):
 pL, nW, nL = '','', []

 for x in range(len(s)):
  if pL == '':
   pL = s[x]
   nW = pL
  else:
   if pL <= s[x]:
    if nW == '':
     nW += pL + s[x]
    else:
     nW += s[x]
    pL = s[x]
   elif s[x] < pL:
    nL.append(nW)
    nW = ''
    pL = s[x]
 
 if nW != '':
  nL.append(nW)
 
 print( max(nL, key=len) )

if __name__ == "__main__":
 main('ijeimcxqxxxhfvvsud')
