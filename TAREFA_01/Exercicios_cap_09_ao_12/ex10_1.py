def nested_sum(t) :
   soma = 0
   for l in t :
      soma += sum(l)
      
   return soma
   

t = [[1,2], [3], [4,5,6]]
s = nested_sum(t)
print(s)
