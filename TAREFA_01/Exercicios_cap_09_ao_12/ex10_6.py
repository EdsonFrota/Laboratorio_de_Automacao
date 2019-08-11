def is_anagram(p1, p2):
   a = sorted(p1)
   b = sorted(p2)
   if a == b :
      return True
   return False

a = 'marrocos'
b = 'socorram'
print(is_anagram(a, b))
