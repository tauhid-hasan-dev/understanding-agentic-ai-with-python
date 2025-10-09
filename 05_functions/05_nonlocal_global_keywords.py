# Be very careful when you use nonlocal and global

chai_type = "ginger"

def understading_non_local_and_global():
    chai_type = "lemon"
    def testing_nonlocal():
        nonlocal chai_type # non local does not work on any global variable, it only works
        chai_type = "tulsi"
        print(f"Converting local to nonlocal from 'lemon' to 'tulsi' : {chai_type}")
        # changing the global variable using "global" keyword
        def testing_global():
            global chai_type
            chai_type = "Black"
            print(f"Converting global from ginger to Black : {chai_type}")
        testing_global()
    testing_nonlocal()
    print("Outside of the testing global function: ", chai_type)

understading_non_local_and_global()

print(f"Global : {chai_type}")


