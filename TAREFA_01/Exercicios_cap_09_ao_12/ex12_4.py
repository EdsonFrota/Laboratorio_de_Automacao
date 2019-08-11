fin = open('/root/words.txt')

def load_dict():
   d = dict() # dicionário palavra => palavra ordenada

   for line in fin:
      word = line.strip()
      d.setdefault(word)
      
   return d
   

def children(word, d):
   b = False
   t = []

   for e in word[1:]:
      w = list(word[1:])
      w.remove(e)
      w.insert(0, word[0])
      w = ''.join(w)

      if w in d:
         t.append(w)
         b = True
         
      
   if b:
      t.sort()
      return t
   return b
   

def load_children(d):
   all = dict()

   for k in d:
      temp = children(k, d)
      if temp:
         all[k] = temp
         
      
   return all
   

def print_all(d):
   for k, v in d.items():
      print(k, v)
      
   

def print_longest(d):
   words = list(d.keys())
   words.sort(key = len, reverse=True)

   b = words[0]
   print(b)
   print(d[b])
   

d = load_dict()
red = load_children(d)
op = int(input('Insira 1 para ver todas as palavras e seus filhos e 2 para a maior palavra e seus filhos'))
if op == 1:
   print_all(red)
elif op == 2:
   print_longest(red)
   

