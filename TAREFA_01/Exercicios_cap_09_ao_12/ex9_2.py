fin = open('/root/words.txt')

def has_no_e(word):
   for c in word:
      if c == 'e':
         return False
         
      
   return True
   

t = 0
c = 0
for line in fin:
   t += 1
   word = line.strip()
   if has_no_e(word):
      c += 1
      print(word)
      
   

print(str((c/t)*100) + '% das palavras não possuem a letra \'e\'')
