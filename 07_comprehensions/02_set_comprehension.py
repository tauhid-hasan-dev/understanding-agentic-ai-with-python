# set comprehension
# {expression for item in iterable if condition}
# set gives unique items by default

menu = ["green tea", "ginger tea", "green tea", "chai", "black tea"]

all_unique_chai = {char for char in menu}
print(all_unique_chai)

recipes = {
    "chai": ["tea", "sugar", "milk", "water"],
    "coffee": ["coffee", "sugar", "milk"],
    "tea": ["tea", "sugar", "water"],
}

# ingredient is the item in the recipe
unique_ingredients = {ingredient for recipe in recipes.values() for ingredient in recipe}
print(unique_ingredients)

