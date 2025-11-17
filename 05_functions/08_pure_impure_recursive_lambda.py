# pure function : always returns the same results for same imputer

def add_numbers(a, b):
    return a + b

# Always returns same result for same inputs
print(add_numbers(5, 3))  # Always 8
print(add_numbers(5, 3))  # Always 8


# impure function ( Different results each time called)
counter = 0

def increment_counter():
    global counter
    counter += 1
    return counter

# Different results each time called
print(increment_counter())  # 1
print(increment_counter())  # 2


# Recursive function (A recursive function in Python is a function that calls itself to solve a problem by breaking it down into smaller, similar subproblems.)
# Recursion is powerful but should be used carefully with proper base cases to avoid infinite loops!
def fibonacci(n):
    # Base cases
    if n <= 1:
        return n
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8 (0, 1, 1, 2, 3, 5, 8)

# lambda function: in Python is an anonymous (unnamed) function that can be defined inline. 
# It's a concise way to create small, single-expression functions.

# Regular Function: Named, can have multiple statements
def multiply(x, y):
    return x * y

# # One-liner, no name
lambda_multiply = lambda x, y: x * y

print(lambda_multiply(55, 66))


# Different use case of lambda function
numbers = [1, 2, 3, 4, 5]

# Using lambda with map()
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Using lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# Using lambda with sorted()
names = ["Alice", "Bob", "Charlie"]
sorted_by_length = sorted(names, key=lambda x: len(x))
print(sorted_by_length)  # ['Bob', 'Alice', 'Charlie']

