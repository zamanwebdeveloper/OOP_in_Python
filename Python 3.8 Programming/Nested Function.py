# nested function
a = 5
def f():
    # a = 5 # Non Local
    def g():
        global a
        a = 6
        return a*a
    print(a,'a*a = ',g())
f()
print(a)