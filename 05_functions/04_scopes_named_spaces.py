# local scope (inside a function)

def serve_chai():
    chai_type = "Masala" 
    print(f"Inside the function : {chai_type}")

# global scope
chai_type = "Lemon" #global scope
serve_chai()
print(f"Outside function : {chai_type}")

# Enclosing scope
def chai_counter():
    chai_order = "lemon" # Enclosing scope
    def print_order():
        chai_order = "Ginger"
        print("Inner:", chai_order)
    print_order()
    print("Outer: ", chai_order)

chai_order = "Tulsi"
print("Global", chai_order)
