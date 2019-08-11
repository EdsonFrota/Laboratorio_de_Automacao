fin = open('/root/words.txt')
count = 0

def load_list():
   r = []

   for line in fin:
      r.append(line.strip())
      
   return r
   

def in_bisect(lista, word, min, max):
   i = (max+min)//2
   global count
   count += 1

   if max < min or not i in range(0, len(lista)):
      return None
      

   if word == lista[i]:
      return i
   elif word < lista[i]:
      return in_bisect(lista, word, min, i-1)
   elif word > lista[i]:
      return in_bisect(lista, word, i+1, max)
      
   

words = load_list()
word = str(input('Insira a palavra que deseja buscar: '))
index = in_bisect(words, word, 0, len(words))

if not index is None:
   print('A palavra se encontra no indice: ' + str(index))
else:
   print('A palavra não se encontra na lista')
   

print('Passos: ' + str(count))
