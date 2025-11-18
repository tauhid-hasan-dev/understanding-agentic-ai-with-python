# Importing from a package (folder with __init__.py)

# Method 1: Import from package level (thanks to __init__.py)
from mypackage import greet

print(greet("Alice"))

# Method 2: Import directly from the module
from mypackage.helper import say_goodbye

print(say_goodbye("Bob"))

