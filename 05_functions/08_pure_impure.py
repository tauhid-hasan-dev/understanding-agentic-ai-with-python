# Pure Function: A function that always returns the same output for the same input and does not have any side effects

def pure_function(x):
    return x * 2

# Impure Function: A function that returns a different output for the same input and has side effects
# Impure functions are not recommended to use because they are not deterministic and not easy to test.

# Example 1: Function with side effect (modifies global state)
counter = 0
def impure_function_with_side_effect(x):
    global counter
    counter += 1  # Side effect: modifies global variable
    print(f"Function called {counter} times")  # Side effect: prints to console
    return x + counter  # Returns different value each time due to side effect

# Example 2: Function that returns different output for same input (uses random)
import random
def impure_function_with_random(x):
    random_value = random.randint(1, 10)  # Different value each call
    return x + random_value  # Same input, different output

# Example 3: Function that uses current time
from datetime import datetime
def impure_function_with_time(x):
    current_time = datetime.now().second  # Different value each second
    return x + current_time  # Same input, different output

