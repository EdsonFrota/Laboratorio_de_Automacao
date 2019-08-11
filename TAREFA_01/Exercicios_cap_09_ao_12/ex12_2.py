fin = open('/root/words.txt')

def load_dict():
   d = dict() # dicionário palavra => palavra ordenada

   for line in fin:
      word = line.strip()

      t = ''.join(sorted(word)) #realiza o sort da string, oque a transforma em list. como list não pode ser key de dict, utiliza join pra retorna a list para string
      d[word] = t
      
   return d
   

def anagrams(d):
   anag_dict = dict()
   l = []

   # inversão do dicionário (chave => valores, valores => chave)
   # palavra ordenada => conjunto de palavras que, quando ordenadas, equivalem a chave
   for k, v in d.items():
      if v in anag_dict:
         anag_dict[v].append(k)
      else:
         anag_dict[v] = [k]
         
      

   # carrega os valores do dicionário (listas de palavras  - não ordenadas - que são anagramas)
   for v in anag_dict.values():
      if len(v) > 1: # se a lista não possui só uma palavra, ou seja, se há anagramas, carrega na lista de anagramas
         l.append(v)
         
      

   l.sort(key = len, reverse=True) # fas o sort utilizando como parâmetro a length de cada lista-elemento da lista

   return l
   

d = load_dict()
a = anagrams(d)

for e in a:
   print(e)
   

