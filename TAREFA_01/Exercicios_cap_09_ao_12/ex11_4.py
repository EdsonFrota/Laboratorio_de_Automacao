def has_duplicates(s):
   d = dict()

   for e in s:
      if e in d:
         return True
         
      d.setdefault(e)
      
   return False
   

l1 = [1, 2, 3, 4, 2]
l2 = ['a', 'c', 'a', 'j']
l3 = [3, 5, 1, 6, 7]

print(has_duplicates(l1))
print(has_duplicates(l2))
print(has_duplicates(l3))

