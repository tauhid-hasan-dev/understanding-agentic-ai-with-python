# Upcasting (widening): Safe and sometimes implicit (e.g., 3 + 2.5 → float).
# Downcasting (narrowing): Must be explicit, may lose precision or give unexpected results.

# Upcasting
print(float(5))       # 5.0
print(complex(5))     # (5+0j)
print(complex(3.2))   # (3.2+0j)
print(int(True))      # 1
print(int(False))     # 0
print(float(True))    # 1.0
print(float(False))   # 0.0

# Downcasting
print(int(9.8))                     # 9
print(float(complex(7, 0).real))  # 7.0
print(bool(1))                # True
print(bool(5))                # True
print(bool(0))                # False
print(int("123"))             # 123
print(float("12.5"))          # 12.5
print(bool("True"))           # True
print(bool("False"))          # True  (non-empty string!)
print(bool(""))               # False (empty string)



is_boiling = True
stri_count = 5

total_action = stri_count + is_boiling # upcasting
print(f"Total action: {total_action}") # 6


# logical operations

warm_water = True
tea_added = True

# and
tea_ready = warm_water and tea_added
print(f"Tea ready: {tea_ready}") # True

# or
tea_ready = warm_water or tea_added
print(f"Tea ready: {tea_ready}") # True

# not
tea_ready = not warm_water
print(f"Tea ready: {tea_ready}") # False