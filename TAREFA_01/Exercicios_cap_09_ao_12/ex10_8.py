import random

def gen_birthdays(n):
   t = []

   for i in range(n):
      t.append(random.randint(1,365))
      
   return t
   

def check_match(t):
   for i in range(len(t)):
      if t[i] in t[i+1:]:
         return True
         
      
   return False
   

def run_simulations(n_simulations, n_pessoas):
   count_matchs = 0

   for i in range(n_simulations):
      t = gen_birthdays(n_pessoas)
      if check_match(t): count_matchs += 1
      
   return count_matchs
   

ns = int(input('Insira o número de simulações que devem ser rodadas: '))
np = int(input('Insira o número de pessoas por simulação: '))
print('')

matchs = run_simulations(ns, np)
p = (matchs/ns)*100
print(str(matchs) + ' matchs em ' + str(ns) + ' simulações com pelo menos 1 match em cada') 
print(str(p) + '% de simulações com pelo menos um match')

