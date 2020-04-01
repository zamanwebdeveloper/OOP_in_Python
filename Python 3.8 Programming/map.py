# function and sequence
# functiion = def haha(x,c,f,d)
                    # return x,c,d,f
# sequence = [2,4,5,2,7,3
# list,set,tuple
def haha(x):
    return x**2
b = [1,2,3,4,5]
a = list(map(haha,b))
print(a)

c = list(map(lambda x:x**2,b))
print(c)

