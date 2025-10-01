# difference bwteen dict and list

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


