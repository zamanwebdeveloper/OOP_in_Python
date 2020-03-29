# String Word Reverse
a = 'i love you'
print(' '.join(a.split()[::-1]))
b = a.split() # list
c = b[::-1]
d = ' '.join(c)
print(b)
print(c)
print(d)