"""
EXPERT EXPLANATION: Tuples in Python

Tuples are immutable sequence data types in Python. They are similar to lists but with
one crucial difference: they cannot be modified after creation. This immutability
makes tuples faster, more memory-efficient, and suitable for specific use cases.

KEY CHARACTERISTICS:
1. IMMUTABLE: Cannot be changed after creation
2. ORDERED: Elements maintain their order
3. INDEXED: Can access elements by index
4. DUPLICATES ALLOWED: Can have duplicate values
5. HETEROGENEOUS: Can contain different data types
6. HASHABLE: Can be used as dictionary keys (if all elements are hashable)

ADVANTAGES OF TUPLES:
- Faster iteration and access
- Less memory usage
- Can be used as dictionary keys
- Thread-safe (immutable)
- Guaranteed data integrity
- Better for function returns

COMMON USE CASES:
- Coordinates (x, y)
- Database records
- Function returns (multiple values)
- Dictionary keys
- Configuration data
- Constants that shouldn't change
"""

print("=" * 60)
print("TUPLES DEMONSTRATION - IMMUTABLE OPERATIONS")
print("=" * 60)

spice_mix = ("cumin", "ginger", "coriander")

more_spice_mix = ("black pepper", "chili powder", "salt") # created for concatenation

print(f"Original spice mix: {spice_mix}")
print(f"More spices: {more_spice_mix}")

# =============================================================================
# 1. TUPLE UNPACKING (Destructuring Assignment)
# =============================================================================
print("\n" + "-" * 40)
print("1. TUPLE UNPACKING")
print("-" * 40)

# Basic unpacking (destructuring)
(spice_1, spice_2, spice_3) = spice_mix
print(f"Spice 1: {spice_1}")
print(f"Spice 2: {spice_2}")
print(f"Spice 3: {spice_3}")

# Multiple assignment (creates tuples implicitly)
ginger_ratio, cumin_ratio = 5, 1
print(f"Ginger ratio: {ginger_ratio}, Cumin ratio: {cumin_ratio}")

# Swap values using tuple unpacking or destructuring (Pythonic way!)
cumin_ratio, ginger_ratio = ginger_ratio, cumin_ratio
print(f"After swap - Ginger ratio: {ginger_ratio}, Cumin ratio: {cumin_ratio}")

# Advanced unpacking with * (star operator) or destructuring
spice_1, *remaining_spices = spice_mix 
print(f"First spice: {spice_1}")
print(f"Remaining spices: {remaining_spices} (type: {type(remaining_spices)})")

# Unpacking with * in the middle or destructuring (remaining elements)  
first, *middle, last = ("a", "b", "c", "d", "e")
print(f"First: {first}, Middle: {middle}, Last: {last}")

# =============================================================================
# 2. TUPLE OPERATIONS
# =============================================================================
print("\n" + "-" * 40)
print("2. TUPLE OPERATIONS")
print("-" * 40)

# Membership testing
print(f"'cumin' in spice_mix: {'cumin' in spice_mix}")
print(f"'paprika' not in spice_mix: {'paprika' not in spice_mix}")

# Length
print(f"Length of spice_mix: {len(spice_mix)}")

# Concatenation (creates new tuple)
combined_spices = spice_mix + more_spice_mix
print(f"Combined spices: {combined_spices}")

# Repetition
doubled_spices = spice_mix * 2
print(f"Doubled spices: {doubled_spices}")

# Indexing and slicing
print(f"First spice: {spice_mix[0]}")
print(f"Last spice: {spice_mix[-1]}")
print(f"First two spices: {spice_mix[:2]}")

# =============================================================================
# 3. IMMUTABILITY DEMONSTRATION
# =============================================================================
print("\n" + "-" * 40)
print("3. IMMUTABILITY DEMONSTRATION")
print("-" * 40)

print("Tuples are immutable - you cannot modify them after creation:")
print(f"Original tuple: {spice_mix}")

# This would cause an error:
# spice_mix[0] = "paprika"  # TypeError: 'tuple' object does not support item assignment

# But you can create new tuples
new_spice_mix = spice_mix + ("paprika",)
print(f"New tuple with paprika: {new_spice_mix}")

# =============================================================================
# 4. TUPLE METHODS
# =============================================================================
print("\n" + "-" * 40)
print("4. TUPLE METHODS")
print("-" * 40)

# count() - count occurrences
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Numbers tuple: {numbers}")
print(f"Count of '2': {numbers.count(2)}")

# index() - find first occurrence
print(f"Index of '2': {numbers.index(2)}")
print(f"Index of '5': {numbers.index(5)}")

# =============================================================================
# 5. REAL-WORLD EXAMPLES
# =============================================================================
print("\n" + "-" * 40)
print("5. REAL-WORLD EXAMPLES")
print("-" * 40)

# Coordinates
point = (10, 20)
print(f"Point coordinates: {point}")

# RGB color
orange_color = (255, 165, 0)
print(f"Orange RGB: {orange_color}")

# Database record
user_record = ("John", 25, "john@email.com", "Engineer")
name, age, email, job = user_record
print(f"User: {name}, Age: {age}, Email: {email}, Job: {job}")

# Function returning multiple values
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {min_val}, Max: {max_val}")

# Using tuples as dictionary keys
coordinate_map = {
    (0, 0): "origin",
    (1, 1): "diagonal",
    (2, 3): "point"
}
print(f"Coordinate map: {coordinate_map}")
print(f"Value at (1,1): {coordinate_map[(1, 1)]}")

# =============================================================================
# 6. PERFORMANCE COMPARISON
# =============================================================================
print("\n" + "-" * 40)
print("6. PERFORMANCE COMPARISON")
print("-" * 40)

import time
import sys

# Create large collections
large_list = list(range(100000))
large_tuple = tuple(range(100000))

# Memory usage
list_memory = sys.getsizeof(large_list)
tuple_memory = sys.getsizeof(large_tuple)
print(f"Memory usage - List: {list_memory:,} bytes, Tuple: {tuple_memory:,} bytes")
print(f"Tuples use {list_memory/tuple_memory:.2f}x less memory")

# Access time
start_time = time.time()
for i in range(1000):
    large_list[i]
list_access_time = time.time() - start_time

start_time = time.time()
for i in range(1000):
    large_tuple[i]
tuple_access_time = time.time() - start_time

print(f"Access time - List: {list_access_time:.6f}s, Tuple: {tuple_access_time:.6f}s")
print(f"Tuples are {list_access_time/tuple_access_time:.2f}x faster for access")

print("\n" + "=" * 60)
print("EXPERT TIP: When to use Tuples vs Lists")
print("=" * 60)
print("Use TUPLES when:")
print("- Data shouldn't change (coordinates, constants)")
print("- Need dictionary keys")
print("- Returning multiple values from functions")
print("- Performance is critical")
print("- Data integrity is important")
print()
print("Use LISTS when:")
print("- Need to modify the collection")
print("- Need list-specific methods (sort, append, etc.)")
print("- Building collections dynamically")
print("- Need mutable behavior")

