#Forwarding function

def add(p,q,r):
    return p+q+r

def add1(p,q,r):
    return p-q+r

def add2(p,q,r):
    return add1(p,q,r)

d1 = [100,20,10]
s = add(*d1)
# s = add(d1[0],d1[1],d1[2])
print(s)
print(add2(*d1))
