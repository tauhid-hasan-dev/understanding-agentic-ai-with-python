def infinite_generator():
    count = 0 
    while True:
        yield f"Refill the {count}th bottle"
        count += 1

refill_bottles = infinite_generator()
refill_bottles_user2 = infinite_generator() 

for _ in range(3):
    print(next(refill_bottles))
 
for _ in range(6):
    print(next(refill_bottles_user2))