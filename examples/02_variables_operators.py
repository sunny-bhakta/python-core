"""
Variables & Operators Examples
===============================
This file demonstrates variables, scoping, and all types of operators in Python.
"""

# ============================================================================
# VARIABLES
# ============================================================================

print("=" * 60)
print("VARIABLES")
print("=" * 60)

# Valid variable names
my_variable = 10
myVariable = 20  # camelCase (not Pythonic, but valid)
_private_var = 30
CONSTANT_VALUE = 100  # Constants convention
variable123 = 40

print(f"my_variable: {my_variable}")
print(f"CONSTANT_VALUE: {CONSTANT_VALUE}")

# Dynamic typing
x = 10
print(f"x = {x}, type: {type(x)}")
x = "Hello"
print(f"x = {x}, type: {type(x)}")
x = [1, 2, 3]
print(f"x = {x}, type: {type(x)}")

# ============================================================================
# VARIABLE SCOPE
# ============================================================================

print("\n" + "=" * 60)
print("VARIABLE SCOPE")
print("=" * 60)

# Global variable
global_var = "I'm global"

def local_scope_example():
    """Demonstrates local scope"""
    local_var = "I'm local"
    print(f"Inside function - global_var: {global_var}")
    print(f"Inside function - local_var: {local_var}")

local_scope_example()
# print(local_var)  # This would cause an error

def modify_global():
    """Demonstrates modifying global variable"""
    global global_var
    global_var = "Modified global"
    print(f"Inside function - global_var: {global_var}")

print(f"Before function - global_var: {global_var}")
modify_global()
print(f"After function - global_var: {global_var}")

def outer_function():
    """Demonstrates nonlocal scope"""
    outer_var = "I'm in outer function"
    
    def inner_function():
        nonlocal outer_var
        outer_var = "Modified in inner function"
        print(f"Inner function - outer_var: {outer_var}")
    
    print(f"Before inner - outer_var: {outer_var}")
    inner_function()
    print(f"After inner - outer_var: {outer_var}")

outer_function()

# ============================================================================
# ARITHMETIC OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("ARITHMETIC OPERATORS")
print("=" * 60)

a, b = 10, 3

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")

# Special cases
print(f"\nDivision by zero handling:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"  10 / 0 raises: {type(e).__name__}")

# ============================================================================
# COMPARISON OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("COMPARISON OPERATORS")
print("=" * 60)

x, y = 5, 10

print(f"x = {x}, y = {y}")
print(f"Equal (x == y): {x == y}")
print(f"Not equal (x != y): {x != y}")
print(f"Less than (x < y): {x < y}")
print(f"Greater than (x > y): {x > y}")
print(f"Less than or equal (x <= y): {x <= y}")
print(f"Greater than or equal (x >= y): {x >= y}")

# Chained comparisons
print(f"\nChained comparisons:")
print(f"1 < 2 < 3: {1 < 2 < 3}")
print(f"1 < 3 < 2: {1 < 3 < 2}")

# ============================================================================
# LOGICAL OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("LOGICAL OPERATORS")
print("=" * 60)

p, q = True, False

print(f"p = {p}, q = {q}")
print(f"AND (p and q): {p and q}")
print(f"OR (p or q): {p or q}")
print(f"NOT (not p): {not p}")
print(f"NOT (not q): {not q}")

# Truth tables
print("\nTruth tables:")
print("AND:")
print(f"  True and True = {True and True}")
print(f"  True and False = {True and False}")
print(f"  False and True = {False and True}")
print(f"  False and False = {False and False}")

print("\nOR:")
print(f"  True or True = {True or True}")
print(f"  True or False = {True or False}")
print(f"  False or True = {False or True}")
print(f"  False or False = {False or False}")

# Short-circuit evaluation
print("\nShort-circuit evaluation:")
def return_true():
    print("  return_true() called")
    return True

def return_false():
    print("  return_false() called")
    return False

print("False and return_true():")
result = False and return_true()  # return_true() not called

print("True or return_false():")
result = True or return_false()  # return_false() not called

# ============================================================================
# ASSIGNMENT OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("ASSIGNMENT OPERATORS")
print("=" * 60)

x = 10
print(f"Initial x = {x}")

x += 5
print(f"After x += 5: {x}")

x -= 3
print(f"After x -= 3: {x}")

x *= 2
print(f"After x *= 2: {x}")

x /= 4
print(f"After x /= 4: {x}")

x = 20
x //= 3
print(f"After x //= 3: {x}")

x = 20
x %= 3
print(f"After x %= 3: {x}")

x = 2
x **= 3
print(f"After x **= 3: {x}")

# ============================================================================
# IDENTITY OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("IDENTITY OPERATORS")
print("=" * 60)

# is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")

print(f"\na == b (value equality): {a == b}")
print(f"a is b (identity equality): {a is b}")
print(f"a is c (identity equality): {a is c}")

# None checking
x = None
y = None
print(f"\nx = None, y = None")
print(f"x == y: {x == y}")
print(f"x is y: {x is y}")
print(f"x is None: {x is None}")

# Small integers (Python caches small integers)
a = 256
b = 256
print(f"\na = 256, b = 256")
print(f"a is b: {a is b}")  # True (cached)

a = 257
b = 257
print(f"a = 257, b = 257")
print(f"a is b: {a is b}")  # May be False (not cached)

# ============================================================================
# MEMBERSHIP OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("MEMBERSHIP OPERATORS")
print("=" * 60)

# In strings
text = "Python"
print(f"text = '{text}'")
print(f"'P' in text: {'P' in text}")
print(f"'p' in text: {'p' in text}")
print(f"'thon' in text: {'thon' in text}")
print(f"'Java' not in text: {'Java' not in text}")

# In lists
numbers = [1, 2, 3, 4, 5]
print(f"\nnumbers = {numbers}")
print(f"3 in numbers: {3 in numbers}")
print(f"10 in numbers: {10 in numbers}")
print(f"10 not in numbers: {10 not in numbers}")

# In dictionaries (checks keys)
person = {"name": "Alice", "age": 30}
print(f"\nperson = {person}")
print(f"'name' in person: {'name' in person}")
print(f"'Alice' in person: {'Alice' in person}")  # False (checks keys, not values)
print(f"'Alice' in person.values(): {'Alice' in person.values()}")

# In sets
fruits = {"apple", "banana", "cherry"}
print(f"\nfruits = {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'orange' not in fruits: {'orange' not in fruits}")

# ============================================================================
# BITWISE OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("BITWISE OPERATORS")
print("=" * 60)

a, b = 5, 3  # 5 = 101, 3 = 011 in binary

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")

print(f"\nBitwise AND (a & b): {a & b} (binary: {bin(a & b)})")
print(f"Bitwise OR (a | b): {a | b} (binary: {bin(a | b)})")
print(f"Bitwise XOR (a ^ b): {a ^ b} (binary: {bin(a ^ b)})")
print(f"Bitwise NOT (~a): {~a} (binary: {bin(~a & 0xFF)})")

print(f"\nLeft shift (a << 1): {a << 1} (binary: {bin(a << 1)})")
print(f"Right shift (a >> 1): {a >> 1} (binary: {bin(a >> 1)})")

# Practical example: flags
READ = 1    # 001
WRITE = 2   # 010
EXECUTE = 4 # 100

permissions = READ | WRITE  # 011
print(f"\nPermissions example:")
print(f"READ = {READ} ({bin(READ)})")
print(f"WRITE = {WRITE} ({bin(WRITE)})")
print(f"EXECUTE = {EXECUTE} ({bin(EXECUTE)})")
print(f"permissions = READ | WRITE = {permissions} ({bin(permissions)})")
print(f"Has READ: {bool(permissions & READ)}")
print(f"Has WRITE: {bool(permissions & WRITE)}")
print(f"Has EXECUTE: {bool(permissions & EXECUTE)}")

# ============================================================================
# OPERATOR PRECEDENCE
# ============================================================================

print("\n" + "=" * 60)
print("OPERATOR PRECEDENCE")
print("=" * 60)

# Examples showing precedence
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1} (multiplication first)")

result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2} (parentheses first)")

result3 = 2 ** 3 * 4
print(f"2 ** 3 * 4 = {result3} (exponentiation first)")

result4 = not True and False
print(f"not True and False = {result4} (not first, then and)")

result5 = True or False and False
print(f"True or False and False = {result5} (and first, then or)")

