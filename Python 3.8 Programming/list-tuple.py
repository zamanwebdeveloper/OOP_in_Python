# list and tuple
a = [1,2,3] # list can read and  write
b = (4,5,6) # tuple can only read
a.append(10)
# b.append(10)
c = tuple(a)
# c.append(12)
d = list(b)
d.append(12)
b = tuple(d)

print('a = ',a)
print('b = ',b)
print('c = ',c)
print('d = ',d)
# print('e = ',e)
