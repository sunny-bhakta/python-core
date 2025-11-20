# Python Core Concepts

A comprehensive guide to all core concepts of Python programming language.

## Table of Contents

1. [Basic Syntax & Data Types](#basic-syntax--data-types)
2. [Variables & Operators](#variables--operators)
3. [Control Flow](#control-flow)
4. [Functions](#functions)
5. [Data Structures](#data-structures)
6. [Object-Oriented Programming](#object-oriented-programming)
7. [Modules & Packages](#modules--packages)
8. [File Handling](#file-handling)
9. [Exception Handling](#exception-handling)
10. [Advanced Topics](#advanced-topics)
11. [Standard Library](#standard-library)
12. [Best Practices](#best-practices)

---

## Basic Syntax & Data Types

### Data Types
- **Numbers**
  - Integers (`int`)
  - Floating-point numbers (`float`)
  - Complex numbers (`complex`)
- **Strings** (`str`)
  - String formatting (f-strings, `.format()`, `%`)
  - String methods (`.upper()`, `.lower()`, `.split()`, `.join()`, etc.)
  - String slicing and indexing
- **Booleans** (`bool`)
  - `True` and `False`
  - Truthiness and falsiness
- **None** (`NoneType`)
  - `None` as a null value

### Type Conversion
- `int()`, `float()`, `str()`, `bool()`
- Type checking with `type()` and `isinstance()`

### Comments
- Single-line comments (`#`)
- Multi-line comments (triple quotes `"""` or `'''`)

---

## Variables & Operators

### Variables
- Variable naming rules
- Dynamic typing
- Variable scope (local, global, nonlocal)

### Operators
- **Arithmetic**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical**: `and`, `or`, `not`
- **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`, etc.
- **Identity**: `is`, `is not`
- **Membership**: `in`, `not in`
- **Bitwise**: `&`, `|`, `^`, `~`, `<<`, `>>`

---

## Control Flow

### Conditional Statements
- `if`, `elif`, `else`
- Ternary operators (conditional expressions)
- Chained comparisons

### Loops
- **`for` loops**
  - Iterating over sequences
  - `range()` function
  - `enumerate()` for index and value
  - `zip()` for parallel iteration
- **`while` loops**
  - Loop control with `break` and `continue`
  - `else` clause in loops

### Loop Control
- `break` - exit loop
- `continue` - skip to next iteration
- `pass` - placeholder statement

---

## Functions

### Function Definition
- `def` keyword
- Function parameters
  - Positional arguments
  - Keyword arguments
  - Default parameters
  - `*args` (variable positional arguments)
  - `**kwargs` (variable keyword arguments)

### Function Types
- Regular functions
- Lambda functions (anonymous functions)
- Recursive functions
- Higher-order functions
- Generator functions (`yield`)

### Function Concepts
- Return values (`return` statement)
- Multiple return values (tuples)
- Function scope and closures
- Decorators (`@decorator`)
- Docstrings (`"""`)

---

## Data Structures

### Lists (`list`)
- Creating lists
- List indexing and slicing
- List methods (`.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`, etc.)
- List comprehensions
- Nested lists

### Tuples (`tuple`)
- Immutable sequences
- Tuple unpacking
- Named tuples (`collections.namedtuple`)

### Dictionaries (`dict`)
- Key-value pairs
- Dictionary methods (`.get()`, `.keys()`, `.values()`, `.items()`, `.update()`, etc.)
- Dictionary comprehensions
- Default dictionaries (`collections.defaultdict`)

### Sets (`set`)
- Unordered collections of unique elements
- Set operations (union, intersection, difference, symmetric difference)
- Set methods (`.add()`, `.remove()`, `.discard()`, `.update()`, etc.)
- Set comprehensions
- Frozen sets (`frozenset`)

### Strings (as sequences)
- String methods and operations
- String formatting
- Regular expressions (`re` module)

---

## Object-Oriented Programming

### Classes & Objects
- Class definition (`class`)
- Object instantiation
- Instance variables
- Class variables
- Methods
  - Instance methods
  - Class methods (`@classmethod`)
  - Static methods (`@staticmethod`)

### Special Methods (Magic/Dunder Methods)
- `__init__()` - constructor
- `__str__()` and `__repr__()` - string representation
- `__len__()`, `__getitem__()`, `__setitem__()`
- `__eq__()`, `__lt__()`, `__gt__()` - comparison operators
- `__add__()`, `__sub__()` - arithmetic operators
- And many more...

### Inheritance
- Single inheritance
- Multiple inheritance
- Method Resolution Order (MRO)
- `super()` function
- Method overriding

### Encapsulation
- Public, protected (`_`), and private (`__`) attributes
- Property decorators (`@property`, `@setter`, `@deleter`)

### Polymorphism
- Duck typing
- Method overriding
- Operator overloading

### Abstract Classes
- `abc` module
- Abstract methods and classes

---

## Modules & Packages

### Modules
- Creating modules (`.py` files)
- Importing modules (`import`, `from ... import`)
- `__name__` and `__main__`
- Module search path
- Standard library modules

### Packages
- Package structure
- `__init__.py`
- Subpackages
- Package imports

### Namespace
- Namespace concepts
- `dir()` function
- `globals()` and `locals()`

---

## File Handling

### File Operations
- Opening files (`open()`)
- File modes (`'r'`, `'w'`, `'a'`, `'x'`, `'b'`, `'t'`, `'+'`)
- Reading files (`.read()`, `.readline()`, `.readlines()`)
- Writing files (`.write()`, `.writelines()`)
- Context managers (`with` statement)
- File closing

### File Paths
- `os.path` module
- `pathlib` module (Path objects)
- Absolute vs relative paths

---

## Exception Handling

### Exception Basics
- `try`, `except`, `else`, `finally` blocks
- Exception types (`ValueError`, `TypeError`, `KeyError`, `IndexError`, etc.)
- Catching specific exceptions
- Catching multiple exceptions
- Exception hierarchy

### Raising Exceptions
- `raise` statement
- Creating custom exceptions
- Exception chaining

### Exception Best Practices
- When to use exceptions
- Exception handling patterns

---

## Advanced Topics

### Comprehensions
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Generator expressions

### Generators
- Generator functions (`yield`)
- Generator expressions
- `next()` and `iter()`
- Generator pipelines

### Iterators
- Iterator protocol
- `__iter__()` and `__next__()`
- Built-in iterators
- Custom iterators

### Context Managers
- `with` statement
- `__enter__()` and `__exit__()`
- `contextlib` module

### Decorators
- Function decorators
- Class decorators
- Decorator patterns
- `functools.wraps`

### Closures
- Nested functions
- Free variables
- Closure scope

### Metaclasses
- Class creation
- `type()` and metaclasses
- `__new__()` and `__init__()`

### Descriptors
- Descriptor protocol
- Property descriptors
- `__get__()`, `__set__()`, `__delete__()`

### Memory Management
- Reference counting
- Garbage collection
- `gc` module
- Circular references

### Concurrency & Parallelism
- Threading (`threading` module)
- Multiprocessing (`multiprocessing` module)
- `asyncio` (asynchronous programming)
- `concurrent.futures`

### Regular Expressions
- `re` module
- Pattern matching
- Groups and capturing
- Search and replace

### Serialization
- `pickle` module
- `json` module
- `csv` module
- `xml` module

---

## Standard Library

### Essential Modules
- **`os`** - Operating system interface
- **`sys`** - System-specific parameters
- **`math`** - Mathematical functions
- **`random`** - Random number generation
- **`datetime`** - Date and time handling
- **`collections`** - Specialized container datatypes
- **`itertools`** - Iterator functions
- **`functools`** - Higher-order functions
- **`operator`** - Standard operators as functions
- **`json`** - JSON encoder and decoder
- **`csv`** - CSV file reading and writing
- **`re`** - Regular expressions
- **`urllib`** - URL handling
- **`http`** - HTTP modules
- **`sqlite3`** - SQLite database interface
- **`logging`** - Logging facility
- **`unittest`** - Unit testing framework
- **`pdb`** - Python debugger
- **`argparse`** - Command-line argument parsing
- **`pathlib`** - Object-oriented filesystem paths
- **`typing`** - Type hints support

---

## Best Practices

### Code Style
- PEP 8 style guide
- Naming conventions
- Code formatting
- Line length and indentation

### Documentation
- Docstrings (PEP 257)
- Comments vs docstrings
- Type hints (PEP 484)

### Testing
- Unit testing
- Test-driven development (TDD)
- `unittest` framework
- `pytest` framework

### Version Control
- Git basics
- `.gitignore` for Python

### Virtual Environments
- `venv` module
- `virtualenv`
- Dependency management (`pip`, `requirements.txt`)

### Package Management
- `pip` - Package installer
- `setuptools` - Package building
- `wheel` - Built-package format
- `pyproject.toml` - Modern project configuration

### Performance
- Profiling (`cProfile`)
- Optimization techniques
- List vs generator trade-offs
- Caching (`functools.lru_cache`)

### Security
- Input validation
- SQL injection prevention
- Secure coding practices

---

## Additional Resources

### Python Enhancement Proposals (PEPs)
- PEP 8 - Style Guide for Python Code
- PEP 20 - The Zen of Python
- PEP 257 - Docstring Conventions
- PEP 484 - Type Hints

### Learning Path
1. Start with basic syntax and data types
2. Master control flow and functions
3. Learn data structures thoroughly
4. Understand object-oriented programming
5. Explore modules and packages
6. Practice file handling and exception handling
7. Dive into advanced topics
8. Study standard library modules
9. Follow best practices and coding standards

---

## Notes

This README covers the fundamental and advanced concepts of Python. Each topic can be explored in depth through practice and building projects. Python's philosophy emphasizes readability, simplicity, and the "batteries included" approach with its extensive standard library.

