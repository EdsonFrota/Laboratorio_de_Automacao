"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def read_dictionary(filename='/root/anaconda3/bin/c06d'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

def is_homophone(w1, w2):
   if w1 in d and w2 in d:
      if d[w1] == d[w2]:
         return True
         
      
   return False
   

d = read_dictionary()

for word in d:
   if len(word) != 5: continue #5 letras
   temp = word[1:]
   if is_homophone(word, temp):
      temp = word[0] + word[2:]
      if is_homophone(word, temp):
         print(word)
         
      
   

