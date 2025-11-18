# Demonstrating the difference between Module and Package

print("=" * 60)
print("MODULE vs PACKAGE")
print("=" * 60)
print()

# ============================================
# MODULE: A single .py file
# ============================================
print("1. MODULE (Single file)")
print("-" * 60)
print("math_utils.py is a MODULE (it's a single .py file)")
print()

# Import a module
import math_utils
print(f"   Imported module: import math_utils")
print(f"   Used it: math_utils.add(5, 3) = {math_utils.add(5, 3)}")
print()

# ============================================
# PACKAGE: A folder with __init__.py
# ============================================
print("2. PACKAGE (Folder with __init__.py)")
print("-" * 60)
print("mypackage/ is a PACKAGE (it's a folder with __init__.py)")
print("  - mypackage/__init__.py  ← Makes it a package")
print("  - mypackage/helper.py     ← Module inside the package")
print()

# Import from a package
from mypackage import greet
print(f"   Imported from package: from mypackage import greet")
print(f"   Used it: greet('Python') = {greet('Python')}")
print()

# ============================================
# SUMMARY
# ============================================
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("MODULE:")
print("  • Single .py file")
print("  • Example: math_utils.py")
print("  • Import: import math_utils")
print()
print("PACKAGE:")
print("  • Folder with __init__.py")
print("  • Example: mypackage/")
print("  • Import: from mypackage import ...")
print("=" * 60)

