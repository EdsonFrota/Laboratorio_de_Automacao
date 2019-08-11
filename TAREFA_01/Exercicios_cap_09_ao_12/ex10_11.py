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
      
   

r = load_list()

for word in r:
   if not in_bisect(r, word[::-1], 0, len(r)) is None:
      print(word)
      
   

print(str(count) + ' comparações')
