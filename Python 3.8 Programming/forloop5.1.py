# Continue Statement
p = [1,2,3,4,12,5,6,7,8]
def continu(list):
    for i in list:
        if i < 10:
            continue
        return i;
print(continu(p))