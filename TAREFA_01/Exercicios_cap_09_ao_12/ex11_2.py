def invert_dic(d):
   r = dict()

   for key in d:
      val = d[key]
      r.setdefault(val, [])
      r[val].append(key)
      
   return r
   

d = {'a' : 1, 'p' : 1, 'r' : 2, 't' : 1, 'o' : 1}

r = invert_dic(d)
print(r)
