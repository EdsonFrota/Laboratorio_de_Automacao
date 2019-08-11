import time

def construct_list_append():
   fin = open('/root/words.txt')
   r = []

   for line in fin:
      r.append(line.strip())
      
   fin.close()
   return r
   

def construct_list_noAppend():
   fin = open('/root/words.txt')
   r = []

   for line in fin:
      r = r + [line.strip()]
      
   fin.close()
   return r
   

start = time.time()
construct_list_append()
et = time.time() - start
print('Com append demorou ' + str(et) + ' segundos') # ~ 0.8 segundo

start = time.time()
construct_list_noAppend()
et = time.time() - start
print('Sem append demorou ' + str(et) + ' segundos') # ~ 54.5 segundos

# Suponho que a segunda (sem append) demore mais para ser executada pois reatribui a lista e todos os seus elementos a si mesma, alem de adicionar o novo elemento
