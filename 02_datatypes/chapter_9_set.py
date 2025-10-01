# Chapter 9: Sets with Union and Intersection Operations
"""
EXPERT EXPLANATION: Sets in Python

Sets are unordered collections of unique elements in Python. Key characteristics:

1. UNIQUENESS: 
   - No duplicate elements allowed
   - Adding duplicates is silently ignored

2. UNORDERED:
   - Elements have no defined order/position
   - Cannot access by index
   - Order may change between operations

3. MUTABLE:
   - Can add/remove elements
   - But elements must be immutable (hashable)

4. FAST OPERATIONS:
   - O(1) lookups using hash tables
   - Efficient for membership testing
   - Perfect for removing duplicates

5. MATHEMATICAL SET OPERATIONS:
   - Union (|)
   - Intersection (&) 
   - Difference (-)
   - Symmetric Difference (^)

Common Use Cases:
- Removing duplicates from sequences
- Membership testing
- Mathematical set operations
- Finding unique/common elements
"""

print("=" * 50)
print("SETS: UNION AND INTERSECTION OPERATIONS")
print("=" * 50)

# Creating sets
print("\n1. Creating Sets:")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {3, 4, 5, 9, 10}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Set 3: {set3}")

# UNION OPERATIONS
print("\n" + "=" * 30)
print("UNION OPERATIONS")
print("=" * 30)

# Method 1: Using | operator
print("\n2. Union using | operator:")
union_result = set1 | set2
print(f"set1 | set2 = {union_result}")

# Method 2: Using union() method
print("\n3. Union using union() method:")
union_result2 = set1.union(set2)
print(f"set1.union(set2) = {union_result2}")

# Union of multiple sets
print("\n4. Union of multiple sets:")
union_all = set1 | set2 | set3
print(f"set1 | set2 | set3 = {union_all}")

# Using union() with multiple sets
union_all_method = set1.union(set2, set3)
print(f"set1.union(set2, set3) = {union_all_method}")

# INTERSECTION OPERATIONS
print("\n" + "=" * 30)
print("INTERSECTION OPERATIONS")
print("=" * 30)

# Method 1: Using & operator
print("\n5. Intersection using & operator:")
intersection_result = set1 & set2
print(f"set1 & set2 = {intersection_result}")

# Method 2: Using intersection() method
print("\n6. Intersection using intersection() method:")
intersection_result2 = set1.intersection(set2)
print(f"set1.intersection(set2) = {intersection_result2}")

# Intersection of multiple sets
print("\n7. Intersection of multiple sets:")
intersection_all = set1 & set2 & set3
print(f"set1 & set2 & set3 = {intersection_all}")

# Using intersection() with multiple sets
intersection_all_method = set1.intersection(set2, set3)
print(f"set1.intersection(set2, set3) = {intersection_all_method}")

# DIFFERENCE OPERATIONS
print("\n" + "=" * 30)
print("DIFFERENCE OPERATIONS")
print("=" * 30)

# Method 1: Using - operator
print("\n8. Difference using - operator:")
difference_result = set1 - set2
print(f"set1 - set2 = {difference_result}")

# Method 2: Using difference() method
print("\n9. Difference using difference() method:")
difference_result2 = set1.difference(set2)
print(f"set1.difference(set2) = {difference_result2}")

# SYMMETRIC DIFFERENCE
print("\n" + "=" * 30)
print("SYMMETRIC DIFFERENCE")
print("=" * 30)

# Method 1: Using ^ operator
print("\n10. Symmetric difference using ^ operator:")
symmetric_diff = set1 ^ set2
print(f"set1 ^ set2 = {symmetric_diff}")

# Method 2: Using symmetric_difference() method
print("\n11. Symmetric difference using symmetric_difference() method:")
symmetric_diff2 = set1.symmetric_difference(set2)
print(f"set1.symmetric_difference(set2) = {symmetric_diff2}")

# PRACTICAL EXAMPLES
print("\n" + "=" * 30)
print("PRACTICAL EXAMPLES")
print("=" * 30)

# Example 1: Student enrollment
print("\n12. Student Enrollment Example:")
math_students = {"Alice", "Bob", "Charlie", "David", "Eve"}
physics_students = {"Bob", "Charlie", "Frank", "Grace", "Henry"}
chemistry_students = {"Alice", "Charlie", "Ivy", "Jack", "Kate"}

print(f"Math students: {math_students}")
print(f"Physics students: {physics_students}")
print(f"Chemistry students: {chemistry_students}")

# Students taking both math and physics
math_physics = math_students & physics_students
print(f"Students taking both Math and Physics: {math_physics}")

# Students taking all three subjects
all_three = math_students & physics_students & chemistry_students
print(f"Students taking all three subjects: {all_three}")

# Students taking at least one science subject
science_students = physics_students | chemistry_students
print(f"Students taking at least one science: {science_students}")

# Students taking only math
only_math = math_students - physics_students - chemistry_students
print(f"Students taking only Math: {only_math}")

# Example 2: Website visitors
print("\n13. Website Visitors Example:")
monday_visitors = {"user1", "user2", "user3", "user4", "user5"}
tuesday_visitors = {"user2", "user3", "user6", "user7", "user8"}
wednesday_visitors = {"user1", "user3", "user9", "user10"}

print(f"Monday visitors: {monday_visitors}")
print(f"Tuesday visitors: {tuesday_visitors}")
print(f"Wednesday visitors: {wednesday_visitors}")

# Unique visitors across all days
unique_visitors = monday_visitors | tuesday_visitors | wednesday_visitors
print(f"Unique visitors across all days: {unique_visitors}")

# Visitors who came on both Monday and Tuesday
monday_tuesday = monday_visitors & tuesday_visitors
print(f"Visitors on both Monday and Tuesday: {monday_tuesday}")

# Visitors who came on all three days
all_days = monday_visitors & tuesday_visitors & wednesday_visitors
print(f"Visitors on all three days: {all_days}")

# SET COMPARISON METHODS
print("\n" + "=" * 30)
print("SET COMPARISON METHODS")
print("=" * 30)

# Subset and Superset
print("\n14. Subset and Superset:")
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {1, 2, 3}

print(f"set_a: {set_a}")
print(f"set_b: {set_b}")
print(f"set_c: {set_c}")

print(f"set_a.issubset(set_b): {set_a.issubset(set_b)}")
print(f"set_b.issuperset(set_a): {set_b.issuperset(set_a)}")
print(f"set_a == set_c: {set_a == set_c}")

# Disjoint sets
print("\n15. Disjoint sets:")
disjoint_set1 = {1, 2, 3}
disjoint_set2 = {4, 5, 6}
print(f"disjoint_set1: {disjoint_set1}")
print(f"disjoint_set2: {disjoint_set2}")
print(f"disjoint_set1.isdisjoint(disjoint_set2): {disjoint_set1.isdisjoint(disjoint_set2)}")

# MUTABLE SET OPERATIONS
print("\n" + "=" * 30)
print("MUTABLE SET OPERATIONS")
print("=" * 30)

# Update operations
print("\n16. Update operations:")
original_set = {1, 2, 3}
print(f"Original set: {original_set}")

# Update with union
original_set.update({4, 5, 6})
print(f"After update with {{4, 5, 6}}: {original_set}")

# Intersection update
original_set.intersection_update({2, 3, 4, 7})
print(f"After intersection_update with {{2, 3, 4, 7}}: {original_set}")

# Difference update
original_set.difference_update({2})
print(f"After difference_update with {{2}}: {original_set}")

# Symmetric difference update
original_set.symmetric_difference_update({3, 8, 9})
print(f"After symmetric_difference_update with {{3, 8, 9}}: {original_set}")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("""
Key Points about Sets:

1. UNION (| or union()):
   - Combines all unique elements from multiple sets
   - Removes duplicates automatically
   - set1 | set2 | set3 or set1.union(set2, set3)

2. INTERSECTION (& or intersection()):
   - Returns elements common to all sets
   - set1 & set2 & set3 or set1.intersection(set2, set3)

3. DIFFERENCE (- or difference()):
   - Returns elements in first set but not in second
   - set1 - set2 or set1.difference(set2)

4. SYMMETRIC DIFFERENCE (^ or symmetric_difference()):
   - Returns elements in either set but not in both
   - set1 ^ set2 or set1.symmetric_difference(set2)

5. COMPARISON METHODS:
   - issubset(), issuperset(), isdisjoint()
   - == for equality comparison

6. MUTABLE OPERATIONS:
   - update(), intersection_update(), difference_update()
   - symmetric_difference_update()

Sets are perfect for:
- Removing duplicates
- Finding common elements
- Mathematical set operations
- Fast membership testing
- Data analysis and filtering
""")
