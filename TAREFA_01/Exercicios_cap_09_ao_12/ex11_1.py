fin = open('/root/words.txt')

def load_dic():
   d = dict()

   for line in fin:
      d[line.strip()] = ''
      
   return d
   

word = str(input('Insira a palavra a ser buscada: '))
d = load_dic()

if word in d:
   print('Palavra está no dicionário')
else:
   print('Palavra não está no dicionário')
   

