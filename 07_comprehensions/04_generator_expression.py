# generator expression
# (expression for item in iterable if condition)

# 
numbers = [1, 2, 3, 4, 5]

# generator is memory efficient
# it doesn't store all the values in memory rather it generates the values on the fly
odd_numbers = sum(number for number in numbers if number % 2 == 0)
print(odd_numbers)








