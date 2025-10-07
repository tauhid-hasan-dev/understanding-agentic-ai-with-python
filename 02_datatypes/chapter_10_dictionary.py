


# What is a Dictionary in Python?
# A dictionary in Python is a collection data type that stores data in key-value pairs. It's similar to a real-world dictionary where you look up a word (key) to find its definition (value).
# Key Characteristics:
# Key-Value Structure: Each item consists of a key and its corresponding value
# Mutable: You can modify dictionaries after creation
# Unordered: Items don't have a fixed order (though Python 3.7+ maintains insertion order)


# # Method 1: Using curly braces
# my_dict = {"key1": "value1", "key2": "value2"}

# # Method 2: Using dict() constructor
# my_dict = dict(key1="value1", key2="value2")

# # Method 3: Empty dictionary
# my_dict = {}

muzlu_sut = dict(type="muzlu_sut", taste="sut", sugar=10)
print("muzlu_sut: ", muzlu_sut)

print(muzlu_sut["type"])
print(muzlu_sut["taste"])
print(muzlu_sut["sugar"])

muzlu_sut["sugar"] = 20
print("muzlu_sut: ", muzlu_sut)

muzlu_sut["salt"] = 1
print("muzlu_sut: ", muzlu_sut)

muzlu_sut.pop("salt")
print("muzlu_sut: ", muzlu_sut)

chai_recipe = {}
chai_recipe["tea"] = 10
chai_recipe["sugar"] = 10
chai_recipe["milk"] = 10
chai_recipe["water"] = 10

print("chai_recipe: ", chai_recipe)

del chai_recipe["water"]
print("chai_recipe: ", chai_recipe)

print("sugar" in chai_recipe)
print("salt" in chai_recipe)

print(len(chai_recipe))

# print(chai_recipe.keys())
# print(chai_recipe.values())
# print(chai_recipe.items())

print(chai_recipe.get("sugar"))
print(chai_recipe.get("salt", "not found")) 

# popitem
last_item = chai_recipe.popitem()
print("last_item: ", last_item)
print("chai_recipe: ", chai_recipe)

# update
chai_recipe.update({"sugar": 20, "milk": 20, "water": 20})
print("chai_recipe: ", chai_recipe)

# clear
chai_recipe.clear()
print("chai_recipe: ", chai_recipe)


