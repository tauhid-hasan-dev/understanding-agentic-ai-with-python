# What is a generator?
# A generator is a function that returns an iterator that produces a sequence of values when iterated over.
# Generators are used to generate a sequence of values, but they do not store all the values in memory, rather they generate the values on the fly.
# Generators are more memory efficient than lists.

# Example of a generator function
# In normal function, return is used to return a value from a function but in generator function, 
# yield is a keyword that is used to generate a value from a generator function.

def my_normal_function():
    return ["apple", "banana", "cherry"]


# my_normal_function_object = my_normal_function()
# print(my_normal_function_object)

def my_generator():
    yield "apple"
    yield "banana"
    yield "cherry"

my_generator_object = my_generator()
print(next(my_generator_object)) # next is a built-in function that is used to get the next value from a generator object.  
print(next(my_generator_object)) # it will return the next value from the generator object.
print(next(my_generator_object))
# print(next(my_generator_object)) # it will raise a StopIteration error because there are no more values to return.

