# Reduce
# Reduction -> Reduce
# Reduce = Binary_function, sequence
from functools import reduce
def func(x,y):
    return x*y
a = [1,2,3,4,5,6]
b = reduce(func,a)
print(b)

