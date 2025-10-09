
numbers = [1, 2, 4]

def edit_number(cup):
    cup[1] = 49

edit_number(numbers)
print(numbers)

# There are two ways of sending arguments 

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

# Positioned arguments
make_chai("Bangladesh", "Yes", "low")

# Named arguments
make_chai(tea="Srilanka", milk="No", sugar="high")

# using both postioned and named arguments using * and ** 
def special_chai(*ingredients, **extras):
    print("Ingredients", type(ingredients), ":", ingredients)
    print("Extras", type(extras),":", extras)

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes")





