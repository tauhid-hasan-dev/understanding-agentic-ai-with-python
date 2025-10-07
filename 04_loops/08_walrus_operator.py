value = 13
# remainder = value % 5

# print(f"Remained: {remainder}")

# if(remainder := value % 5):
#     print(f"not divisiable, remainder is {remainder}")

# available_sizes = ['large', 'medium', 'small']

# if(requested_size := input("Enter you chai cup: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")

# print(f"Size is unavailable - {requested_size}")


flavors = ["masala", "ginger", "karak", "minit"]

print ("Avialable flavours: ", flavors)

while (flavor := input("Choose your flavor: ")) not in flavors:
    print (f"Sorry, {flavor} is not avialable")

print(f"You choose {flavor} chai")




