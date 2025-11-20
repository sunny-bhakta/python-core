"""
Modules & Packages Examples
============================
This file demonstrates module creation, importing, and package structure.
"""

# ============================================================================
# CREATING A SIMPLE MODULE
# ============================================================================

# This would be in a separate file: math_utils.py
# For demonstration, we'll create it here

import sys
import os

# Create a simple module file for demonstration
math_utils_code = '''
"""Math utilities module"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

PI = 3.14159
E = 2.71828
'''

# Write the module file
with open('math_utils.py', 'w') as f:
    f.write(math_utils_code)

print("=" * 60)
print("MODULES")
print("=" * 60)

# ============================================================================
# IMPORTING MODULES
# ============================================================================

# Import entire module
import math_utils
print(f"5 + 3 = {math_utils.add(5, 3)}")
print(f"5 * 3 = {math_utils.multiply(5, 3)}")
print(f"PI = {math_utils.PI}")

# Import with alias
import math_utils as mu
print(f"\nUsing alias: 10 - 4 = {mu.subtract(10, 4)}")

# Import specific items
from math_utils import add, multiply
print(f"\nDirect import: 7 + 8 = {add(7, 8)}")

# Import all (not recommended)
from math_utils import *
print(f"Import all: 6 * 7 = {multiply(6, 7)}")

# ============================================================================
# __name__ AND __main__
# ============================================================================

print("\n" + "=" * 60)
print("__name__ AND __main__")
print("=" * 60)

# Create a module that checks __name__
main_demo_code = '''
def main():
    print("This is the main function")

if __name__ == "__main__":
    print("Running as main script")
    main()
else:
    print("Imported as module")
'''

with open('main_demo.py', 'w') as f:
    f.write(main_demo_code)

# When imported, __name__ is the module name
import main_demo
print(f"Module __name__ when imported: {main_demo.__name__}")

# ============================================================================
# STANDARD LIBRARY MODULES
# ============================================================================

print("\n" + "=" * 60)
print("STANDARD LIBRARY MODULES")
print("=" * 60)

# os module
import os
print(f"Current directory: {os.getcwd()}")
print(f"OS name: {os.name}")

# sys module
import sys
print(f"Python version: {sys.version.split()[0]}")
print(f"Platform: {sys.platform}")

# math module
import math
print(f"\nMath module:")
print(f"  pi = {math.pi}")
print(f"  e = {math.e}")
print(f"  sqrt(16) = {math.sqrt(16)}")
print(f"  sin(pi/2) = {math.sin(math.pi/2)}")

# random module
import random
print(f"\nRandom module:")
print(f"  Random int 1-10: {random.randint(1, 10)}")
print(f"  Random float: {random.random()}")
numbers = [1, 2, 3, 4, 5]
print(f"  Random choice: {random.choice(numbers)}")
random.shuffle(numbers)
print(f"  Shuffled: {numbers}")

# datetime module
from datetime import datetime, timedelta
print(f"\nDatetime module:")
now = datetime.now()
print(f"  Current time: {now}")
print(f"  Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
tomorrow = now + timedelta(days=1)
print(f"  Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")

# json module
import json
data = {"name": "Alice", "age": 30, "city": "NYC"}
json_str = json.dumps(data)
print(f"\nJSON module:")
print(f"  Original: {data}")
print(f"  JSON string: {json_str}")
parsed = json.loads(json_str)
print(f"  Parsed back: {parsed}")

# collections module
from collections import Counter, defaultdict, deque
print(f"\nCollections module:")
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)
print(f"  Word count: {counter}")

dd = defaultdict(int)
dd["a"] += 1
print(f"  Defaultdict: {dict(dd)}")

dq = deque([1, 2, 3])
dq.appendleft(0)
print(f"  Deque: {list(dq)}")

# ============================================================================
# NAMESPACE
# ============================================================================

print("\n" + "=" * 60)
print("NAMESPACE")
print("=" * 60)

# dir() function
print("Current namespace (first 10 items):")
current_names = [name for name in dir() if not name.startswith('_')]
print(f"  {current_names[:10]}")

print("\nMath module namespace (first 10 items):")
math_names = [name for name in dir(math) if not name.startswith('_')]
print(f"  {math_names[:10]}")

# globals() and locals()
x = 10
y = 20

def test_function():
    local_var = 5
    print(f"  Local variables: {list(locals().keys())}")

print("\nGlobal variables (sample):")
global_vars = {k: v for k, v in globals().items() if not k.startswith('_') and not callable(v)}
print(f"  {list(global_vars.keys())[:5]}")

test_function()

# ============================================================================
# PACKAGE STRUCTURE DEMONSTRATION
# ============================================================================

print("\n" + "=" * 60)
print("PACKAGE STRUCTURE")
print("=" * 60)

# Create a simple package structure
os.makedirs('mypackage', exist_ok=True)
os.makedirs('mypackage/subpackage', exist_ok=True)

# Create __init__.py files
with open('mypackage/__init__.py', 'w') as f:
    f.write('"""My package"""\n__version__ = "1.0.0"\n')

with open('mypackage/subpackage/__init__.py', 'w') as f:
    f.write('"""Subpackage"""\n')

# Create module files
with open('mypackage/module1.py', 'w') as f:
    f.write('def function1():\n    return "Function 1"\n')

with open('mypackage/module2.py', 'w') as f:
    f.write('def function2():\n    return "Function 2"\n')

with open('mypackage/subpackage/module3.py', 'w') as f:
    f.write('def function3():\n    return "Function 3"\n')

# Import from package
try:
    from mypackage import module1
    from mypackage.module2 import function2
    from mypackage.subpackage import module3
    
    print(f"Package import: {module1.function1()}")
    print(f"Direct import: {function2()}")
    print(f"Subpackage import: {module3.function3()}")
except ImportError as e:
    print(f"Import error (expected in some environments): {e}")

# Cleanup
import shutil
for file in ['math_utils.py', 'main_demo.py']:
    if os.path.exists(file):
        os.remove(file)
if os.path.exists('mypackage'):
    shutil.rmtree('mypackage')

print("\nNote: Package structure created and demonstrated above")

