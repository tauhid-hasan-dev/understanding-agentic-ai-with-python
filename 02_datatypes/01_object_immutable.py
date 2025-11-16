# Mutable and Immutable Data Types
# Mutable data types are those that can be changed after they are created. 
# Immutable data types are those that cannot be changed after they are created.
# Mutable data types: list, dictionary, set
# Immutable data types: string, tuple, int, float, bool (value cannot be changed but reference can be changed)


sugar_amount = 10
print(f"I need {sugar_amount} cups of sugar")

sugar_amount = 100
print(f"I need {sugar_amount} cups of sugar")

print(f"The id of the 10 is {id(10)}")
print(f"The id of the 100 is {id(100)}")
