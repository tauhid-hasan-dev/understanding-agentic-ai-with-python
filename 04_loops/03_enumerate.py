# What is enumerate?
# enumerate() is a built-in Python function that adds a counter to an 
# iterable (like a list, tuple, or string) and returns it as an enumerate 
# object. It's very useful when you need both the index and the value of items in a sequence.

# Basic syntax
# enumerate(iterable, start=0)

# list
menu = ["biriyani", 'meat', 'dal']

x = enumerate(menu)

print(f"x is : {x}")

# Instead of this (old way):
for i in range(len(menu)):
    print(f"The old way -> {i}: {menu[i]}")

# Use this (Pythonic way):
for index, item in enumerate(menu, start=1):
    print(f"The pythonic way ==> {index}: {item}")


# finding position of a specific item
for index, item in enumerate(menu, start=1):
    if item == 'biriyani':
        print(f"Found biriyani at position {index}")

for item in menu:
    print(f"Menu item is {item}")