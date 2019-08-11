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
      
   

def is_interlocked(word, passos=2):
   wp = word[::passos] # se 'B, A, T, A, T, A' => 'B, T, T'
   wi = word[1::passos] # se 'B, A, T, A, T, A' => 'A, A, A'

   if not in_bisect(r, wp, 0, len(r)) is None and not in_bisect(r, wi, 0, len(r)) is None:
      print(wp + '   +   ' + wi)
      return True
   else:
      return False
      
   

r = load_list()

for e in r:
   if is_interlocked(e):
      print(e)
      
   

#for e in r:
#   if is_interlocked(e, 3):
#      print(e)
      
   



