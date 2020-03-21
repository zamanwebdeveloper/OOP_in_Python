# recursion
# factorial(n) = 1*2*3*...*n
# factorial(1) = 1
# factorial(n) = n*factorial(n-1) = n
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)



print(factorial(4))
