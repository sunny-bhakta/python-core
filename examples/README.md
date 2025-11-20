# Python Core Concepts - Examples Index

This directory contains comprehensive code examples for all Python core concepts.

## Example Files

1. **01_basic_syntax_data_types.py**
   - Numbers (int, float, complex)
   - Strings and string methods
   - Booleans and truthiness
   - None type
   - Type conversion
   - Comments

2. **02_variables_operators.py**
   - Variable naming and scope
   - All operator types
   - Operator precedence
   - Practical examples

3. **03_control_flow.py**
   - Conditional statements
   - for and while loops
   - break, continue, pass
   - else clause in loops
   - Practical examples

4. **04_functions.py**
   - Function definition
   - Parameters (*args, **kwargs)
   - Return values
   - Lambda functions
   - Recursion
   - Generators
   - Decorators
   - Closures

5. **05_data_structures.py**
   - Lists and list methods
   - Tuples and tuple unpacking
   - Dictionaries
   - Sets and set operations
   - Practical examples

6. **06_oop.py**
   - Classes and objects
   - Instance, class, static methods
   - Special methods
   - Inheritance
   - Encapsulation
   - Polymorphism
   - Abstract classes

7. **07_modules_packages.py**
   - Creating modules
   - Importing modules
   - Standard library modules
   - Package structure
   - Namespace

8. **08_file_handling.py**
   - File operations
   - Reading and writing
   - Context managers
   - File paths (os.path, pathlib)
   - Binary files

9. **09_exception_handling.py**
   - try-except blocks
   - Exception types
   - Raising exceptions
   - Custom exceptions
   - Exception chaining

10. **10_advanced_topics.py**
    - Comprehensions (list, dict, set)
    - Generators
    - Iterators
    - Context managers
    - Decorators
    - Closures
    - Metaclasses
    - Regular expressions
    - Serialization

11. **11_standard_library.py**
    - os, sys modules
    - math, random modules
    - datetime module
    - json, csv modules
    - re module
    - collections module
    - itertools, functools modules
    - logging, pathlib, typing modules

## Running Examples

### Run a single example:
```bash
python examples/01_basic_syntax_data_types.py
```

### Run all examples:
```bash
# On Unix/Linux/Mac
for file in examples/*.py; do python "$file"; done

# On Windows
for %f in (examples\*.py) do python "%f"
```

### Run with Python 3 explicitly:
```bash
python3 examples/01_basic_syntax_data_types.py
```

## Notes

- Examples are self-contained and can be run independently
- Some examples create temporary files that are cleaned up automatically
- Examples demonstrate both basic and advanced usage
- Each example includes comments explaining the concepts
- Modify and experiment with the code to deepen understanding

## Learning Path

1. Start with basic concepts (01-03)
2. Learn functions and data structures (04-05)
3. Understand OOP (06)
4. Explore modules and file handling (07-08)
5. Master exception handling (09)
6. Dive into advanced topics (10)
7. Explore standard library (11)

