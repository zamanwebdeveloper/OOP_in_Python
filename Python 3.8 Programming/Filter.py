# Filter
# Filter = function, sequence
def haha(x):
    return x%2 == 0
a = [1,2,3,4,5,6,7,8,9,10]
r = list(filter(haha,a))
print(r)
