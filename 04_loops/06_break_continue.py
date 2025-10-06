flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavor in flavours:
    if flavor == "Out of Stock":
        continue #skip this 
    if flavor == "Discontinued":
        break #end the entire loop
    print(f"{flavor} is found")

print("Out of the loop")