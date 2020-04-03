# Exception Handling - find
try:
    a = int(input("Enter a Number = "))
    print(10 / a)
except ZeroDivisionError:
    print('divided by zero')
    # another code
