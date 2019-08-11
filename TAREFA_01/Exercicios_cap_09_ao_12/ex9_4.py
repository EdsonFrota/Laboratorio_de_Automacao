#fin = open('/root/words.txt')

def uses_only(letters, word):
   for c in word:
      if not c in letters:
         return False
         
      
   return True

word = str(input('Insira a palavra: '))
letters = list(str(input('Insira as letas obrigatórias: ')))

print(uses_only(letters, word))
