# What is a generator?
# A generator is a function that returns an iterator that produces a sequence of values when iterated over.
# Generators are used to generate a sequence of values, but they do not store all the values in memory, rather they generate the values on the fly.
# Generators are more memory efficient than lists.

# Example of a generator function
def my_generator():
    yield 1
    yield 2
    yield 3

# Example of using a generator
for value in my_generator():
    print(value)

# Example of a generator expression