def sum(a, b):
    return a+b


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


print(sum(4, 55))
print(factorial(4))
