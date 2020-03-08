# print nth fibonacci number
# 0 1 1 2 3 5 8 13 21

def fibonacci(n):
    first = 0
    second = 1
    fibo = 0

    print(first)
    print(second)

    i = 3
    while i <= 10:
        fibo = first + second
        print(fibo)
        first = second
        second = fibo
        i = i + 1

a = int(input("Enter a number = "))
fibonacci(a)