fin = open('/root/words.txt')

def is_abecedarian(word):
   for i in range(1, len(word)):
      if not word[i-1] <= word[i]:
         return False
         
      
   return True
   
c = 0

for line in fin:
   if is_abecedarian(line.strip()):
      c += 1
      
   

print(str(c) + ' palavras em ordem alfabética')
