# What is for-else in Python?
# The for-else construct is a unique feature in Python where the else clause executes 
# only when the for loop completes normally (i.e., without encountering a break statement).

# This will execute the else block
for num in [1, 2, 3, 4, 5]:
    print(f"Processing: {num}")
else:
    print("Loop completed normally")  # This WILL print

# This will NOT execute the else block
for num in [1, 2, 3, 4, 5]:
    if num == 3:
        break
    print(f"Processing: {num}")
else:
    print("This won't print")  # This will NOT print