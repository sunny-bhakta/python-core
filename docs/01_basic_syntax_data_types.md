# Basic Syntax & Data Types

## Overview
Python is a dynamically-typed language, meaning you don't need to declare variable types explicitly. Python automatically determines the type based on the value assigned.

## Data Types

### Numbers

#### Integers (`int`)
Integers are whole numbers, positive or negative, without decimals.

**Characteristics:**
- No size limit (only limited by available memory)
- Can use underscores for readability: `1_000_000`
- Supports binary (`0b`), octal (`0o`), and hexadecimal (`0x`) notation

#### Floating-Point Numbers (`float`)
Floating-point numbers are real numbers with decimal points.

**Characteristics:**
- Represented using decimal notation or scientific notation
- Limited precision (about 15-17 decimal digits)
- Can use `float('inf')` for infinity and `float('nan')` for "not a number"

#### Complex Numbers (`complex`)
Complex numbers have a real and imaginary part.

**Characteristics:**
- Format: `a + bj` where `a` is real part and `b` is imaginary part
- Access parts with `.real` and `.imag` attributes

### Strings (`str`)

Strings are sequences of characters enclosed in quotes.

**Characteristics:**
- Immutable (cannot be changed in place)
- Can use single quotes (`'`), double quotes (`"`), or triple quotes (`"""` or `'''`)
- Triple quotes allow multi-line strings
- Support indexing and slicing
- Many built-in methods for manipulation

**String Formatting Methods:**
1. **f-strings** (Python 3.6+): `f"Hello {name}"`
2. **`.format()` method**: `"Hello {}".format(name)`
3. **% formatting**: `"Hello %s" % name`

**Common String Methods:**
- `.upper()`, `.lower()`, `.title()`, `.capitalize()`
- `.strip()`, `.lstrip()`, `.rstrip()`
- `.split()`, `.join()`
- `.replace()`, `.find()`, `.index()`
- `.startswith()`, `.endswith()`
- `.isalpha()`, `.isdigit()`, `.isalnum()`

### Booleans (`bool`)

Booleans represent truth values: `True` or `False`.

**Characteristics:**
- Subclass of `int` (True = 1, False = 0)
- Case-sensitive: must be `True` or `False`
- Used in conditional statements and logical operations

**Truthiness and Falsiness:**
- **Falsy values**: `False`, `None`, `0`, `0.0`, `0j`, `''`, `[]`, `{}`, `()`
- **Truthy values**: Everything else

### None (`NoneType`)

`None` represents the absence of a value.

**Characteristics:**
- Only one instance of `None` exists (singleton)
- Used to indicate "no value" or "null"
- Returned by functions that don't explicitly return a value

## Type Conversion

Python provides built-in functions to convert between types:

- `int()` - Convert to integer
- `float()` - Convert to float
- `str()` - Convert to string
- `bool()` - Convert to boolean
- `list()` - Convert to list
- `tuple()` - Convert to tuple
- `set()` - Convert to set
- `dict()` - Convert to dictionary

**Type Checking:**
- `type()` - Returns the type of an object
- `isinstance()` - Checks if object is instance of a type (preferred)

## Comments

Comments are used to document code and are ignored by the interpreter.

- **Single-line**: Use `#` for single-line comments
- **Multi-line**: Use triple quotes `"""` or `'''` for multi-line comments (technically docstrings)

## Best Practices

1. Use meaningful variable names
2. Follow PEP 8 style guide
3. Use type hints for better code documentation
4. Prefer f-strings for string formatting (Python 3.6+)
5. Use `isinstance()` instead of `type()` for type checking

