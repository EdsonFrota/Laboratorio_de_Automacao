def is_sorted(t):
   for e in range(1, len(t)):
      if not t[e-1] <= t[e]:
         return False
         
      
   return True
   

t = [1, 2, 3]
print(is_sorted(t))
u = ['a', 'c']
print(is_sorted(u))
v = ['b', 'a']
print(is_sorted(v))

