fin = open('/root/words.txt')

def uses_all(letters, word):
   for c in letters:
      if not c in word:
         return False
         
      
   return True
   

letters = list(str(input('Insira as letras: ')))
c = 0

for line in fin:
   if uses_all(letters, list(line.strip())):
      c += 1
      
   


print(str(c) + ' palavras usam todas as letras definidas')
