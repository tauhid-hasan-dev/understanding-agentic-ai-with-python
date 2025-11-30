# Why should we close generators?
# 1. Resource cleanup - Generators can hold resources (file handles, network connections, etc.)
# 2. Exception handling - Closing triggers cleanup code in finally blocks
# 3. Prevents further iteration - Once closed, generator cannot be used again
# 4. Memory management - Helps Python's garbage collector clean up generator state

# Example 1: Basic closing
def my_generator():
    yield "apple"
    yield "banana"
    yield "cherry"

gen = my_generator()
print(next(gen))  # apple
print(next(gen))  # banana

gen.close()  # Close the generator
# print(next(gen))  # This will raise StopIteration error

# Example 2: Resource cleanup with finally block
def file_reader_generator(filename):
    """Generator that simulates reading a file"""
    try:
        print(f"Opening {filename}")
        # Simulate opening a file
        file_handle = open(filename, 'r')
        for line in file_handle:
            yield line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")
    finally:
        print(f"Closing {filename} - cleanup code executed")
        # In real scenario, we would close the file handle here
        # file_handle.close()

# Using the generator
reader = file_reader_generator("example.txt")
try:
    print(next(reader))
except StopIteration:
    pass
finally:
    reader.close()  # This triggers the finally block in the generator

# Example 3: Generator with cleanup that only runs when closed
def resource_generator():
    """Generator that manages a resource"""
    resource_id = "RES-12345"
    print(f"Resource {resource_id} acquired")
    try:
        yield "data1"
        yield "data2"
        yield "data3"
    finally:
        print(f"Resource {resource_id} released - cleanup executed")

# Without closing - resource might not be released properly
gen1 = resource_generator()
print(next(gen1))  # data1
# If we don't close, the finally block won't execute until garbage collection

# With closing - explicit cleanup
gen2 = resource_generator()
print(next(gen2))  # data1
gen2.close()  # This triggers the finally block immediately

# Example 4: Closing prevents further iteration
def count_generator():
    count = 0
    while count < 5:
        yield count
        count += 1

counter = count_generator()
print(next(counter))  # 0
print(next(counter))  # 1
counter.close()
# After closing, any attempt to use the generator will raise StopIteration
try:
    print(next(counter))  # This will raise StopIteration
except StopIteration:
    print("Generator is closed - cannot iterate further")