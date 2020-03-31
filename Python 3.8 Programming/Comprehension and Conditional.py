# List comprehension
# a = {x|x E N and x is even number and 1<=x<=10}
a = [x for x in range(1,11)if x%2 == 0]
print(a)
a = [x**2 for x in range(1,11)if x%2 == 0]
print(a)
a = [x**2+x for x in range(1,11)if x%2 == 0]
# expression, range/enumerate = f(x) = x^2, condition
print(a)
