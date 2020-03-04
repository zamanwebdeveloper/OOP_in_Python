a = 40
b = 50
c = 60
if a > b:
    if a > c:
        print("a is greatest")
    else:
        print("c is greatest")
elif b > c:
    if b > a:
        print("b is greatest")
    else:
        print("a is greatest")
else:
    print("c is greatest")