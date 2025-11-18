# Python Import - Simple Examples

## Files

- **math_utils.py** - A simple module with functions
- **01_basic_import.py** - Shows: `import module`
- **02_from_import.py** - Shows: `from module import function`
- **04_named_import.py** - Shows: `import module as alias` (named imports)
- **05_module_vs_package.py** - Visual demonstration of module vs package
- **03_import_package.py** - Shows: importing from packages (folders with `__init__.py`)
- **mypackage/** - A simple package example with `__init__.py`
- **`__pycache__/`** - Auto-generated folder (you can ignore it)

## How to Run

```bash
python3 01_basic_import.py
python3 02_from_import.py
python3 04_named_import.py
python3 05_module_vs_package.py
python3 03_import_package.py
```

## Module vs Package

### What is a Module?

A **module** is a single Python file (`.py` file) that contains code you can import.

**Example:**

- `math_utils.py` ← This is a module
- Contains functions like `add()`, `multiply()`

**How to use:**

```python
import math_utils
```

### What is a Package?

A **package** is a folder that contains multiple modules and has an `__init__.py` file.

**Example:**

```
mypackage/          ← This is a package (it's a folder)
  ├── __init__.py   ← Required file that makes it a package
  └── helper.py     ← This is a module inside the package
```

**How to use:**

```python
from mypackage import greet
# or
from mypackage.helper import greet
```

### Simple Comparison

|                | Module                        | Package                     |
| -------------- | ----------------------------- | --------------------------- |
| **What it is** | Single `.py` file             | Folder with `__init__.py`   |
| **Example**    | `math_utils.py`               | `mypackage/`                |
| **Contains**   | Functions, classes, variables | Multiple modules            |
| **Import**     | `import math_utils`           | `from mypackage import ...` |

**Think of it this way:**

- **Module** = A single file (like a single document)
- **Package** = A folder with multiple files (like a folder of documents)

## Three Ways to Import

### Method 1: Import entire module

```python
import math_utils
result = math_utils.add(5, 3)
```

### Method 2: Import specific functions

```python
from math_utils import add
result = add(5, 3)
```

### Method 3: Named import (using alias)

```python
import math_utils as math
result = math.add(5, 3)
```

Or alias specific functions:

```python
from math_utils import add as addition
result = addition(5, 3)
```

## About `__pycache__` Folder

The `__pycache__` folder is **automatically created** by Python when you import modules.

- **What it contains**: Compiled bytecode files (`.pyc` files) - a faster version of your Python code
- **Why it exists**: Python stores compiled code here to make imports faster next time
- **Should you worry?**: **No!** You can safely ignore it or delete it. Python will recreate it when needed
- **Should you commit it?**: Usually **no** - add it to `.gitignore` if using git

**In simple terms**: It's like Python's "cache" to speed things up. You don't need to do anything with it!

## About `__init__.py` File

The `__init__.py` file makes a **folder into a Python package**.

- **What it does**: Tells Python "this folder is a package, you can import from it"
- **Can it be empty?**: Yes! Even an empty `__init__.py` makes a folder a package
- **What can you put in it?**: Code that runs when the package is imported, or imports to make things easier to access

**Example structure:**

```
mypackage/
  ├── __init__.py    ← Makes it a package
  └── helper.py      ← Module inside the package
```

**Without `__init__.py`**: Python won't recognize the folder as a package
**With `__init__.py`**: You can do `from mypackage import something`

See `03_import_package.py` for a working example!
