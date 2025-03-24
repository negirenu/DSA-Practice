def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)


print("factorial of num is:", fact(4))
