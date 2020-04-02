# in or not in
# in/not in -> boolean -> true / false
a = {1:2,'apple':4,'orange':6}
b = input('Enter input here = ')
if b not in a:
    print('There is no ',b,'item')
else:
    print(b, '=', a[b])