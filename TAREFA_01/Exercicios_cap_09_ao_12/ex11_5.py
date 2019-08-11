fin = open('/root/words.txt')

def load_dic():
   d = dict()

   for line in fin:
      word = line.strip()
      d.setdefault(word)
      
   return d
   

def rotate_word(word, n):
   cif = ''

   for c in word:
      cif += chr(ord(c) + n)
      
   return cif
   

words = load_dic()

for word in words:
   for i in range(1, 25):
      cif = rotate_word(word, i)
      if cif in words:
         print(cif + '   +   ' + word)
         
      
   

