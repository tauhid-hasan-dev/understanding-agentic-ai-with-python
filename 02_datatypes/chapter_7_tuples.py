spice_mix = ("cumin", "ginger", "coriander")

more_spice_mix = ("black pepper", "chili powder", "salt") # created for concatenation

(spice_1, spice_2, spice_3) = spice_mix

print(f"Spice 1: {spice_1}")
print(f"Spice 2: {spice_2}")
print(f"Spice 3: {spice_3}")


ginger_ratio, cumin_ratio = 5,1

print(f"Ginger ratio: {ginger_ratio}, Cumin ratio: {cumin_ratio}")

# swap values
cumin_ratio, ginger_ratio = ginger_ratio, cumin_ratio
print(f"Ginger ratio: {ginger_ratio}, Cumin ratio: {cumin_ratio}")

# unpacking (tuple unpacking)
spice_1, spice_2, spice_3 = spice_mix
print(f"Spice 1: {spice_1}")
print(f"Spice 2: {spice_2}")
print(f"Spice 3: {spice_3}")

# unpacking with * (tuple unpacking)
# in Python, * is used in unpacking assignments.
# It collects the “rest” of the values into a list, not a tuple.

spice_1, *spice_2 = spice_mix 
print(f"Spice 1: {spice_1}")
print(f"Rest of the values: {spice_2}")

# membeship testing
print("cumin" in spice_mix)
print("cumin" not in spice_mix)

# length of the tuple
print(len(spice_mix))

# concatenation
print(spice_mix + more_spice_mix)

# repetition
print(spice_mix * 2)

