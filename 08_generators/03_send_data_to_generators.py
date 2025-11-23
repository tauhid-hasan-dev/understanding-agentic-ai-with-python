def my_generator():
    print("Welcome to the generator")
    order = yield
    while True:
        print(f"You ordered {order}")
        # this will pause the generator and return the value to the caller, because of the yield keyword.
        # yield only accepts one argument with send method, so we need to send the value to the generator.
        order = yield 

stall = my_generator()
next(stall) # start the generator

stall.send("Masala chai") # send data to the generator
stall.send("Ginger chai") # send data to the generator
stall.send("Caramel chai") # send data to the generator
