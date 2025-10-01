"""
EXPERT EXPLANATION: Lists vs Tuples in Python

Lists and Tuples are both sequence data types in Python, but they have fundamental differences
that make them suitable for different use cases. Understanding these differences is crucial
for writing efficient and maintainable Python code.

KEY DIFFERENCES:

1. MUTABILITY (Most Important Difference):
   - Lists: MUTABLE - can be modified after creation
   - Tuples: IMMUTABLE - cannot be modified after creation

2. SYNTAX:
   - Lists: Use square brackets []
   - Tuples: Use parentheses () or no brackets at all

3. PERFORMANCE:
   - Lists: Slower for iteration and access (due to mutability overhead)
   - Tuples: Faster for iteration and access (optimized for immutability)

4. MEMORY USAGE:
   - Lists: More memory overhead (need to track mutability)
   - Tuples: Less memory overhead (fixed size, immutable)

5. USE CASES:
   - Lists: When you need to modify the collection (add, remove, change items)
   - Tuples: When you need a fixed collection (coordinates, database records, function returns)

6. HASHABILITY:
   - Lists: NOT hashable (cannot be used as dictionary keys)
   - Tuples: Hashable (can be used as dictionary keys, if all elements are hashable)

7. METHODS:
   - Lists: Many methods (append, remove, insert, sort, reverse, etc.)
   - Tuples: Fewer methods (count, index only)

HETEROGENEOUS DATA:
Both lists and tuples can store different data types in the same collection.
This is called "heterogeneous" data storage.
"""

# Example of heterogeneous data storage
my_list = [1, "hello", 3.14, True, [1, 2, 3]]  # Valid list with multiple types
my_tuple = (1, "hello", 3.14, True, (1, 2, 3)) # Valid tuple with multiple types

print("Heterogeneous List:", my_list)
print("Heterogeneous Tuple:", my_tuple)
print()


# =============================================================================
# PRACTICAL EXAMPLES: Lists (Mutable Operations)
# =============================================================================

print("=" * 60)
print("LISTS DEMONSTRATION - MUTABLE OPERATIONS")
print("=" * 60)

ingredients = ["ginger", "cumin", "coriander"]
print(f"Original ingredients: {ingredients}")

# 1. ADDING ITEMS (Multiple ways)
ingredients.append("black pepper")  # Add to end
print(f"After append: {ingredients}")

ingredients.insert(1, "garlic")  # Insert at specific position
print(f"After insert at position 1: {ingredients}")

ingredients.extend(["salt", "pepper"])  # Add multiple items at the end of the list
print(f"After extend: {ingredients}")

# 2. REMOVING ITEMS (Multiple ways)
ingredients.remove("black pepper")  # Remove by value
print(f"After remove 'black pepper': {ingredients}")

popped_item = ingredients.pop()  # Remove and return last item
print(f"Popped item: {popped_item}")
print(f"After pop: {ingredients}")

popped_item = ingredients.pop(0)  # Remove and return item at index
print(f"Popped item at index 0: {popped_item}")
print(f"After pop(0): {ingredients}")

# 3. MODIFYING ITEMS
ingredients[0] = "fresh ginger"  # Direct assignment
print(f"After modifying first item: {ingredients}")

# 4. SORTING AND REVERSING
ingredients.sort()  # Sort in place
print(f"After sorting: {ingredients}")

ingredients.reverse()  # Reverse in place
print(f"After reversing: {ingredients}")

# 5. LIST COMPREHENSION (Advanced)
squared_numbers = [x**2 for x in range(5)]
print(f"Squared numbers: {squared_numbers}")

# 6. COPYING LISTS
original = [1, 2, 3]
shallow_copy = original.copy()  # or original[:]
deep_copy = original[:]
original.append(4)
print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")

print("\n" + "=" * 60)
print("PERFORMANCE AND MEMORY CONSIDERATIONS")
print("=" * 60)

# Performance comparison
import time

# Large list operations
large_list = list(range(1000000))
start_time = time.time()
sum(large_list)
list_time = time.time() - start_time

large_tuple = tuple(range(1000000))
start_time = time.time()
sum(large_tuple)
tuple_time = time.time() - start_time

print(f"Sum of 1M items - List: {list_time:.6f}s, Tuple: {tuple_time:.6f}s")
print(f"Tuples are {list_time/tuple_time:.2f}x faster for iteration")

# Memory usage
import sys
list_memory = sys.getsizeof([1, 2, 3, 4, 5])
tuple_memory = sys.getsizeof((1, 2, 3, 4, 5))
print(f"Memory usage - List: {list_memory} bytes, Tuple: {tuple_memory} bytes")
print(f"Tuples use {list_memory/tuple_memory:.2f}x less memory")

print("\n" + "=" * 60)
print("HASHABILITY DEMONSTRATION")
print("=" * 60)

# Lists are NOT hashable
try:
    hash([1, 2, 3])
except TypeError as e:
    print(f"Lists are not hashable: {e}")

# Tuples ARE hashable (if all elements are hashable)
tuple_hash = hash((1, 2, 3))
print(f"Tuple hash: {tuple_hash}")

# Using tuples as dictionary keys
coordinates_dict = {
    (0, 0): "origin",
    (1, 1): "diagonal",
    (2, 3): "point"
}
print(f"Dictionary with tuple keys: {coordinates_dict}")

print("\n" + "=" * 60)
print("REAL-WORLD USE CASES")
print("=" * 60)

# Lists: Dynamic data that changes
shopping_cart = ["apples", "bananas"]
shopping_cart.append("oranges")  # Customer adds more items
shopping_cart.remove("bananas")  # Customer removes items
print(f"Shopping cart (dynamic): {shopping_cart}")

# Tuples: Fixed data that shouldn't change
rgb_color = (255, 128, 0)  # Orange color - shouldn't change
coordinates = (10, 20)  # Point coordinates - fixed
print(f"RGB color (fixed): {rgb_color}")
print(f"Coordinates (fixed): {coordinates}")

# Function returning multiple values (tuples)
def get_name_age():
    return ("John", 25)  # Returns a tuple

name, age = get_name_age()  # Tuple unpacking
print(f"Name: {name}, Age: {age}")