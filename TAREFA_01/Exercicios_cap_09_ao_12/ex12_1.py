fin = open('/root/words.txt')

def most_frequent(s):
   d = dict()

   for c in s:
      if c.isalpha():
         d[c] = d.get(c, 0) + 1 #se c nao existe, cria chave a atribui valor 0, seguindo de soma por um. Se c existe soma 1 no valor já salvo
         
      
   #print(d)
   t = []

   for letter, count in d.items():
      t.append((count, letter))
      

   t.sort(reverse=True)
   #print(t)

   return t
   

s = fin.read()
r = most_frequent(s)
for e in r:
   print(e[1])
   

