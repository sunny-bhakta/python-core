# Modules & Packages

## Overview
Modules and packages help organize Python code into reusable components. A module is a single Python file, and a package is a directory containing multiple modules.

## Modules

### Creating Modules
A module is simply a Python file (`.py`) containing definitions and statements.

**Example: `math_utils.py`**
```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

### Importing Modules

**Import entire module:**
```python
import module_name
module_name.function()
```

**Import with alias:**
```python
import module_name as alias
alias.function()
```

**Import specific items:**
```python
from module_name import function1, function2
function1()
```

**Import all:**
```python
from module_name import *
```

### __name__ and __main__

When a module is run directly, `__name__` is `"__main__"`. When imported, it's the module name.

```python
if __name__ == "__main__":
    # Code runs only when executed directly
    pass
```

### Module Search Path
Python searches for modules in:
1. Current directory
2. Directories in `PYTHONPATH`
3. Standard library directories
4. Site-packages directory

## Packages

### Package Structure
A package is a directory containing:
- `__init__.py` file (can be empty)
- Python modules (`.py` files)
- Subpackages (subdirectories)

**Example structure:**
```
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

### __init__.py
- Makes directory a package
- Can be empty or contain initialization code
- Controls what's imported with `from package import *`

### Importing from Packages

```python
from package import module
from package.module import function
from package.subpackage import module
```

## Namespace

### dir() Function
Returns list of names in current namespace or object.

```python
dir()  # Current namespace
dir(module)  # Module's namespace
```

### globals() and locals()
- `globals()` - Returns dictionary of global namespace
- `locals()` - Returns dictionary of local namespace

## Standard Library Modules

Python comes with extensive standard library. Common modules:
- `os` - Operating system interface
- `sys` - System-specific parameters
- `math` - Mathematical functions
- `random` - Random number generation
- `datetime` - Date and time
- `json` - JSON encoder/decoder
- `csv` - CSV file handling
- `re` - Regular expressions
- `collections` - Specialized data structures
- `itertools` - Iterator functions
- `functools` - Higher-order functions

## Best Practices

1. Use descriptive module names
2. Keep modules focused (single responsibility)
3. Use `if __name__ == "__main__"` for executable code
4. Avoid `from module import *` (pollutes namespace)
5. Use packages for larger projects
6. Document modules with docstrings
7. Follow naming conventions (lowercase with underscores)
8. Use `__init__.py` to control package imports
9. Organize related functionality together
10. Use absolute imports when possible

