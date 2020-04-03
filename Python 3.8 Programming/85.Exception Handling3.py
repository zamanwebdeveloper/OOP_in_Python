# Exception Handling - find
try:
    # a = int(input("Enter a Number = "))
    print(10 / a)
    print(10 / b)
    print(10 / '2')
except (ZeroDivisionError,TypeError,NameError):
    print('Invalid you code')
