def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def teste():
    print(fibonacci(4))
    # deve devolver => 3
    print(fibonacci(2))
    # deve devolver => 1
