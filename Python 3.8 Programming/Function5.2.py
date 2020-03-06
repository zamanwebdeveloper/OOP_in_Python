def get_greatest_no(a,b,c):
    greatest = 0
    if a>b:
        if a>c:
            greatest = a
        else:
            greatest = c
    elif b>a:
        if b>c:
            greatest = b
        else:
            greatest = c
    else:
        greatest = c
    return greatest
print("Enter a =")
a = int(input())
print("Enter b =")
b = int(input())
print("Enter c =")
c = int(input())
d = get_greatest_no(a,b,c)
print(d,"is greatest")