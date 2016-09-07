#!/usr/bin/python

def main(s):
 x, y, new_word = 0, 0, ''
 while y + 1 < len(s):
  #print(s[y] + " <= " + s[y+1] + " and " + str(y) + " + 1 < " + str(len(s)))
  while s[y] <= s[y+1] and y + 1 <= len(s):
   new_word += s[y]
   if y + 2 >= len(s) and s[y+1] > s[y]:
    new_word += s[y+1]
   break
  y += 1
 print(new_word)

if __name__ == "__main__":
 main('ytsabcdefghij')
