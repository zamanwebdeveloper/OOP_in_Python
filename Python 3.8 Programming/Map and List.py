# Map and List || Comprehension
def sqr(x):
    return x**2
a = [1,2,3,4,5]
print(list(sqr(x) for x in a))