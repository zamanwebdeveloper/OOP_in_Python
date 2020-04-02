# in or not in
# in/not in -> boolean -> true / false
a = {1:2,'apple':4,5:6}
b = input('Enter input here = ')
if b in a:
    print(b,'=',a[b])
else:
    print('There is no ',b,'item')