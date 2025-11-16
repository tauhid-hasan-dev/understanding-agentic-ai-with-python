# Recursive Functions: A function that calls itself

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# Lambda Functions: A function that is defined without a name

factorial_lambda = lambda n: 1 if n == 0 else n * factorial_lambda(n-1)