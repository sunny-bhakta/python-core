"""
Basic Syntax & Data Types Examples
===================================
This file demonstrates all basic data types and syntax in Python.
"""

# ============================================================================
# NUMBERS
# ============================================================================

print("=" * 60)
print("NUMBERS")
print("=" * 60)

# Integers
integer_num = 42
negative_int = -10
large_int = 1_000_000  # Underscores for readability
binary_num = 0b1010    # Binary: 10
octal_num = 0o755      # Octal: 493
hex_num = 0xFF         # Hexadecimal: 255

print(f"Integer: {integer_num}, Type: {type(integer_num)}")
print(f"Large integer with underscores: {large_int}")
print(f"Binary 0b1010 = {binary_num}")
print(f"Octal 0o755 = {octal_num}")
print(f"Hexadecimal 0xFF = {hex_num}")

# Floating-Point Numbers
float_num = 3.14
scientific = 1.5e3      # 1500.0
negative_float = -2.5
infinity = float('inf')
not_a_number = float('nan')

print(f"\nFloat: {float_num}, Type: {type(float_num)}")
print(f"Scientific notation 1.5e3 = {scientific}")
print(f"Infinity: {infinity}")
print(f"NaN: {not_a_number}")

# Complex Numbers
complex_num = 3 + 4j
complex_from_func = complex(3, 4)

print(f"\nComplex: {complex_num}, Type: {type(complex_num)}")
print(f"Real part: {complex_num.real}")
print(f"Imaginary part: {complex_num.imag}")
print(f"Complex from function: {complex_from_func}")

# ============================================================================
# STRINGS
# ============================================================================

print("\n" + "=" * 60)
print("STRINGS")
print("=" * 60)

# String creation
single_quote = 'Hello, World!'
double_quote = "Hello, World!"
triple_quote = """This is a
multi-line string
that spans multiple lines"""

print(f"Single quote: {single_quote}")
print(f"Double quote: {double_quote}")
print(f"Multi-line:\n{triple_quote}")

# String indexing and slicing
text = "Python"
print(f"\nOriginal: {text}")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"Slice [0:3]: {text[0:3]}")
print(f"Slice [2:]: {text[2:]}")
print(f"Slice [:4]: {text[:4]}")
print(f"Reverse: {text[::-1]}")

# String methods
sample = "  Hello, Python World!  "
print(f"\nOriginal: '{sample}'")
print(f"Upper: {sample.upper()}")
print(f"Lower: {sample.lower()}")
print(f"Title: {sample.title()}")
print(f"Capitalize: {sample.capitalize()}")
print(f"Stripped: '{sample.strip()}'")
print(f"Left stripped: '{sample.lstrip()}'")
print(f"Right stripped: '{sample.rstrip()}'")

# String splitting and joining
words = "apple,banana,cherry"
split_words = words.split(",")
print(f"\nSplit by comma: {split_words}")
joined = " | ".join(split_words)
print(f"Joined with ' | ': {joined}")

# String replacement
text = "Hello World"
replaced = text.replace("World", "Python")
print(f"\nReplace: '{text}' -> '{replaced}'")

# String checking methods
test_strings = ["Hello123", "Hello", "123", "Hello World"]
for s in test_strings:
    print(f"\n'{s}':")
    print(f"  isalpha(): {s.isalpha()}")
    print(f"  isdigit(): {s.isdigit()}")
    print(f"  isalnum(): {s.isalnum()}")
    print(f"  startswith('Hello'): {s.startswith('Hello')}")
    print(f"  endswith('123'): {s.endswith('123')}")

# String formatting methods
name = "Alice"
age = 30

# f-strings (Python 3.6+)
formatted1 = f"My name is {name} and I am {age} years old"
print(f"\nf-string: {formatted1}")

# .format() method
formatted2 = "My name is {} and I am {} years old".format(name, age)
formatted3 = "My name is {n} and I am {a} years old".format(n=name, a=age)
print(f".format(): {formatted2}")
print(f".format() with names: {formatted3}")

# % formatting (older style)
formatted4 = "My name is %s and I am %d years old" % (name, age)
print(f"% formatting: {formatted4}")

# ============================================================================
# BOOLEANS
# ============================================================================

print("\n" + "=" * 60)
print("BOOLEANS")
print("=" * 60)

# Boolean values
true_value = True
false_value = False

print(f"True: {true_value}, Type: {type(true_value)}")
print(f"False: {false_value}, Type: {type(false_value)}")
print(f"True as int: {int(True)}")
print(f"False as int: {int(False)}")

# Truthiness and Falsiness
falsy_values = [False, None, 0, 0.0, 0j, '', [], {}, ()]
print("\nFalsy values:")
for val in falsy_values:
    print(f"  {repr(val)}: {bool(val)}")

truthy_values = [True, 1, -1, 3.14, "hello", [1, 2], {"key": "value"}]
print("\nTruthy values:")
for val in truthy_values:
    print(f"  {repr(val)}: {bool(val)}")

# ============================================================================
# NONE
# ============================================================================

print("\n" + "=" * 60)
print("NONE")
print("=" * 60)

none_value = None
print(f"None: {none_value}, Type: {type(none_value)}")
print(f"None is None: {none_value is None}")

# Function returning None
def no_return():
    pass

result = no_return()
print(f"Function with no return: {result}")

# ============================================================================
# TYPE CONVERSION
# ============================================================================

print("\n" + "=" * 60)
print("TYPE CONVERSION")
print("=" * 60)

# Converting to different types
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
bool_val = bool(num_int)

print(f"String '{num_str}' -> int: {num_int}, type: {type(num_int)}")
print(f"String '{num_str}' -> float: {num_float}, type: {type(num_float)}")
print(f"Int {num_int} -> bool: {bool_val}, type: {type(bool_val)}")

# Converting float to int (truncates)
pi = 3.14159
pi_int = int(pi)
print(f"Float {pi} -> int: {pi_int}")

# Converting to string
number = 42
number_str = str(number)
print(f"Int {number} -> string: '{number_str}', type: {type(number_str)}")

# Type checking
value = 42
print(f"\nType checking for {value}:")
print(f"  type(value): {type(value)}")
print(f"  type(value) == int: {type(value) == int}")
print(f"  isinstance(value, int): {isinstance(value, int)}")
print(f"  isinstance(value, (int, float)): {isinstance(value, (int, float))}")

# ============================================================================
# COMMENTS
# ============================================================================

print("\n" + "=" * 60)
print("COMMENTS")
print("=" * 60)

# Single-line comment
# This is a single-line comment

# Multiple single-line comments
# Line 1
# Line 2
# Line 3

"""
This is a multi-line comment
using triple quotes.
It can span multiple lines.
"""

'''
This is also a multi-line comment
using single triple quotes.
'''

print("Comments are ignored by the interpreter")

# Inline comment
result = 2 + 2  # This adds two numbers

