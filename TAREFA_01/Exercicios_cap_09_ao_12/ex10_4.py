def chop(t):
   t.pop(0)
   t.pop(-1)
   

t = [1, 2, 3, 4]
r = chop(t)
print(r)
print(t)
