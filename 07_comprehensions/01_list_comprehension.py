menu = ["green tea", "ginger tea", "chai"]

# list comprehension
# [expression for item in iterable if condition]
# expression: first "item"

gingered_tea = [item for item in menu if "ginger" in item]
tea_length = [item for item in menu if len(item) > 5]

print(gingered_tea)
print(tea_length)
