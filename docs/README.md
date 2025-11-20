# Python Core Concepts - Documentation Index

This directory contains detailed documentation for all Python core concepts.

## Documentation Files

1. [Basic Syntax & Data Types](01_basic_syntax_data_types.md)
   - Numbers, strings, booleans, None
   - Type conversion
   - Comments

2. [Variables & Operators](02_variables_operators.md)
   - Variable naming and scope
   - Arithmetic, comparison, logical operators
   - Assignment, identity, membership, bitwise operators

3. [Control Flow](03_control_flow.md)
   - Conditional statements (if, elif, else)
   - Loops (for, while)
   - Loop control (break, continue, pass)
   - else clause in loops

4. [Functions](04_functions.md)
   - Function definition and parameters
   - Return values
   - Lambda functions
   - Recursion
   - Decorators
   - Scope and closures

5. [Data Structures](05_data_structures.md)
   - Lists
   - Tuples
   - Dictionaries
   - Sets
   - Strings as sequences

6. [Object-Oriented Programming](06_oop.md)
   - Classes and objects
   - Methods (instance, class, static)
   - Special methods
   - Inheritance
   - Encapsulation
   - Polymorphism
   - Abstract classes

7. [Modules & Packages](07_modules_packages.md)
   - Creating and importing modules
   - Package structure
   - Namespace
   - Standard library overview

8. [File Handling](08_file_handling.md)
   - File operations
   - Reading and writing
   - Context managers
   - File paths (os.path, pathlib)

9. [Exception Handling](09_exception_handling.md)
   - try-except blocks
   - Exception types
   - Raising exceptions
   - Custom exceptions
   - Exception chaining

10. [Advanced Topics](10_advanced_topics.md)
    - Comprehensions
    - Generators
    - Iterators
    - Context managers
    - Decorators
    - Closures
    - Metaclasses
    - Descriptors
    - Memory management
    - Concurrency & parallelism
    - Regular expressions
    - Serialization

11. [Standard Library](11_standard_library.md)
    - Essential modules (os, sys, math, random, etc.)
    - Collections
    - Itertools
    - Functools
    - JSON, CSV
    - Logging
    - And more

## Corresponding Examples

Each documentation file has a corresponding example file in the `examples/` directory:

- `examples/01_basic_syntax_data_types.py`
- `examples/02_variables_operators.py`
- `examples/03_control_flow.py`
- `examples/04_functions.py`
- `examples/05_data_structures.py`
- `examples/06_oop.py`
- `examples/07_modules_packages.py`
- `examples/08_file_handling.py`
- `examples/09_exception_handling.py`
- `examples/10_advanced_topics.py`
- `examples/11_standard_library.py`

## How to Use

1. Read the documentation for a concept
2. Study the corresponding example file
3. Run the examples to see them in action
4. Modify and experiment with the code

## Running Examples

To run an example file:

```bash
python examples/01_basic_syntax_data_types.py
```

Or run all examples:

```bash
for file in examples/*.py; do python "$file"; done
```

