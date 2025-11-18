# Named import: Using 'as' to give imports a different name (alias)

# Method 1: Import module with alias
import math_utils as math

# Use the alias instead of the full module name
result = math.add(5, 3)
print(f"5 + 3 = {result}")

result = math.multiply(4, 2)
print(f"4 * 2 = {result}")

# Method 2: Import function with alias
from math_utils import add as addition, multiply as times

# Use the aliased function names
result = addition(10, 5)
print(f"10 + 5 = {result}")

result = times(3, 7)
print(f"3 * 7 = {result}")

