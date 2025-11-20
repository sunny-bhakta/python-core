# Functions

## Overview
Functions are reusable blocks of code that perform a specific task. They help organize code, reduce repetition, and make programs more modular.

## Function Definition

### Basic Syntax

```python
def function_name(parameters):
    """Docstring"""
    # function body
    return value
```

**Key Components:**
- `def` keyword
- Function name (follows variable naming rules)
- Parameters (optional, in parentheses)
- Colon (`:`) after parameters
- Indented function body
- Optional `return` statement

### Function Parameters

#### Positional Arguments
Arguments passed in order, matched to parameters by position.

```python
def greet(name, age):
    return f"{name} is {age} years old"
```

#### Keyword Arguments
Arguments passed by parameter name.

```python
greet(age=30, name="Alice")  # Order doesn't matter
```

#### Default Parameters
Parameters with default values.

```python
def greet(name, age=18):
    return f"{name} is {age} years old"
```

**Important:** Default parameters are evaluated once when function is defined, not each call.

#### *args (Variable Positional Arguments)
Collects extra positional arguments into a tuple.

```python
def sum_all(*args):
    return sum(args)
```

#### **kwargs (Variable Keyword Arguments)
Collects extra keyword arguments into a dictionary.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

#### Combining Parameter Types
Order: positional, *args, keyword-only, **kwargs

```python
def func(pos1, pos2, *args, kw1, kw2=default, **kwargs):
    pass
```

## Return Values

### Single Return Value
```python
def add(a, b):
    return a + b
```

### Multiple Return Values
Returns a tuple (can be unpacked).

```python
def get_name_age():
    return "Alice", 30

name, age = get_name_age()
```

### No Return Value
Functions without `return` return `None`.

## Function Types

### Regular Functions
Standard function definitions.

### Lambda Functions (Anonymous Functions)
Short, single-expression functions.

**Syntax:**
```python
lambda parameters: expression
```

**Characteristics:**
- No `return` statement (expression is returned)
- Can't contain statements, only expressions
- Often used with `map()`, `filter()`, `sorted()`

### Recursive Functions
Functions that call themselves.

**Key Points:**
- Must have base case (stopping condition)
- Each call should move toward base case
- Can be memory intensive for deep recursion

### Higher-Order Functions
Functions that take other functions as arguments or return functions.

**Common Examples:**
- `map(function, iterable)`
- `filter(function, iterable)`
- `reduce(function, iterable)`

### Generator Functions
Functions that use `yield` instead of `return`.

**Characteristics:**
- Return generator objects
- Lazy evaluation (values generated on demand)
- Memory efficient for large sequences
- Can be iterated with `for` loops

## Function Scope

### Local Scope
Variables defined inside function are local.

### Global Scope
Access global variables with `global` keyword.

```python
x = 10
def func():
    global x
    x = 20
```

### Nonlocal Scope
Access variables in enclosing (non-global) scope.

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
```

### Closures
Inner functions that remember variables from enclosing scope.

## Decorators

Decorators modify or enhance functions without changing their code.

**Syntax:**
```python
@decorator
def function():
    pass
```

**Characteristics:**
- Functions that take functions as arguments
- Return modified or wrapped functions
- Use `@functools.wraps` to preserve metadata

**Common Uses:**
- Timing functions
- Logging
- Caching
- Access control
- Input validation

## Docstrings

Documentation strings that describe functions.

**Conventions:**
- Triple quotes `"""`
- First line: brief description
- Optional detailed description
- Optional parameter/return descriptions

**Access:** `function.__doc__` or `help(function)`

## Best Practices

1. Use descriptive function names (verbs)
2. Keep functions small and focused (single responsibility)
3. Use docstrings for documentation
4. Prefer explicit over implicit
5. Limit number of parameters (consider using classes or dictionaries)
6. Use type hints for better documentation
7. Avoid mutable default arguments
8. Use `return` statements explicitly
9. Consider generator functions for large sequences
10. Use decorators for cross-cutting concerns

