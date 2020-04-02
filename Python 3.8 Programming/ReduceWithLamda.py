# Reduce
# Reduction -> Reduce
# Reduce = Binary_function, sequence
from functools import reduce
a = [1,2,3,4,5,6]
b = reduce(lambda x,y:x*y,a)
print(b)
b = reduce(lambda x,y:x*y,[1,2,3,4,5])
print('x*y result = ',b)
b = reduce(lambda x,y:x+y,[1,2,3,4,5])
print('x+y result = ',b)

