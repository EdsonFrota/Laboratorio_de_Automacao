fin = open('/root/words.txt')

def avoids(letters, word):
   for c in letters:
      for k in word:
         if k == c:
            return False
            
         
      
   return True
   

letters = list(str(input('Insira a lista de 5 letras proibidas: ')))
c = 0

for line in fin:
   word = list(line.strip())
   if avoids(letters, word):
      print(line)
      c += 1
      
   

print(str(c) + ' palavras sem as letras proibidas.')
