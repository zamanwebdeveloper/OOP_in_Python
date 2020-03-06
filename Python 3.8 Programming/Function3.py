def print_greatest_no(a,b,c):
    if a>b:
        if a>c:
            print(a, "is greatest")
        else:
            print(c,"is greatest")
    elif b>a:
        if b>c:
            print(b,"is greatest")
        else:
            print(c,"is greatest")
    else:
        print(c,"is greatest")

a = 40
b = 50
c = 60
print_greatest_no(a,b,c)