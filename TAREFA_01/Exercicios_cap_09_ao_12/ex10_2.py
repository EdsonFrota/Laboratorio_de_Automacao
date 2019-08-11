def cumsum(t):
   r = []
   for i in range(len(t)):
      soma = 0
      for j in range(i+1):
          soma += t[j]
         
      r.append(soma)
      
   return(r)
   

t = [1, 2, 3]
soma = cumsum(t)
print(soma)
