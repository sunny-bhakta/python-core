# Advanced Topics

## Overview
Advanced Python topics include comprehensions, generators, iterators, decorators, context managers, and more sophisticated programming patterns.

## Comprehensions

### List Comprehensions
Concise way to create lists.

**Syntax:**
```python
[expression for item in iterable]
[expression for item in iterable if condition]
```

**Benefits:**
- More readable
- Often faster than loops
- Pythonic

### Dictionary Comprehensions
Create dictionaries concisely.

**Syntax:**
```python
{key: value for item in iterable}
{key: value for item in iterable if condition}
```

### Set Comprehensions
Create sets concisely.

**Syntax:**
```python
{expression for item in iterable}
{expression for item in iterable if condition}
```

### Generator Expressions
Like list comprehensions but lazy (memory efficient).

**Syntax:**
```python
(expression for item in iterable)
```

## Generators

### Generator Functions
Functions that use `yield` instead of `return`.

**Characteristics:**
- Return generator objects
- Lazy evaluation
- Memory efficient
- Can be iterated once

**Syntax:**
```python
def generator():
    yield value
```

### Generator Methods
- `next()` - Get next value
- `send(value)` - Send value to generator
- `close()` - Close generator
- `throw()` - Raise exception in generator

### Generator Pipelines
Chain generators for data processing.

## Iterators

### Iterator Protocol
Objects that implement `__iter__()` and `__next__()`.

**Built-in Iterators:**
- Lists, tuples, strings
- Dictionaries (keys, values, items)
- Files
- `range()`, `enumerate()`, `zip()`

### Creating Custom Iterators

```python
class MyIterator:
    def __iter__(self):
        return self
    
    def __next__(self):
        # Return next value or raise StopIteration
        pass
```

### iter() Function
Convert iterable to iterator.

## Context Managers

### with Statement
Ensures proper resource management.

**Syntax:**
```python
with context_manager as variable:
    # code
```

### Creating Context Managers

**Class-based:**
```python
class MyContextManager:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # cleanup
        return False
```

**Function-based (contextlib):**
```python
from contextlib import contextmanager

@contextmanager
def my_context():
    # setup
    yield resource
    # cleanup
```

## Decorators

### Function Decorators
Modify or enhance functions.

**Syntax:**
```python
@decorator
def function():
    pass
```

**Implementation:**
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper
```

### Class Decorators
Modify or enhance classes.

### Decorator Patterns
- Timing
- Logging
- Caching
- Validation
- Retry logic

### functools.wraps
Preserves function metadata.

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## Closures

### Nested Functions
Functions defined inside other functions.

### Free Variables
Variables from enclosing scope used in nested function.

### Closure Scope
Closures remember variables from enclosing scope even after function returns.

## Metaclasses

### Class Creation
Classes are objects created by metaclasses.

### type() Function
Can create classes dynamically.

**Syntax:**
```python
MyClass = type('MyClass', (BaseClass,), {'attribute': value})
```

### Custom Metaclasses
```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Custom class creation
        return super().__new__(cls, name, bases, dct)
```

## Descriptors

### Descriptor Protocol
Objects that define `__get__()`, `__set__()`, `__delete__()`.

**Types:**
- Data descriptors (define `__set__`)
- Non-data descriptors (only `__get__`)

### Property Descriptors
`@property` uses descriptor protocol.

## Memory Management

### Reference Counting
Python uses reference counting for memory management.

### Garbage Collection
Automatic memory management.

**gc Module:**
- `gc.collect()` - Force collection
- `gc.get_count()` - Get counts
- `gc.set_threshold()` - Set thresholds

### Circular References
Objects referencing each other.

## Concurrency & Parallelism

### Threading
Multiple threads in single process.

**threading Module:**
- `Thread` class
- `Lock` for synchronization
- `Queue` for thread communication

### Multiprocessing
Multiple processes (true parallelism).

**multiprocessing Module:**
- `Process` class
- `Pool` for process pools
- `Queue` for inter-process communication

### asyncio
Asynchronous programming.

**Concepts:**
- Coroutines
- Event loop
- `async`/`await`
- `asyncio.run()`

### concurrent.futures
High-level interface for concurrent execution.

## Regular Expressions

### re Module
Pattern matching and text processing.

**Common Functions:**
- `re.search()` - Find pattern
- `re.match()` - Match at start
- `re.findall()` - Find all matches
- `re.sub()` - Replace matches
- `re.compile()` - Compile pattern

**Pattern Syntax:**
- `.` - Any character
- `*` - Zero or more
- `+` - One or more
- `?` - Zero or one
- `[]` - Character class
- `()` - Groups
- `|` - Alternation

## Serialization

### pickle Module
Python object serialization.

**Functions:**
- `pickle.dump()` - Serialize to file
- `pickle.load()` - Deserialize from file
- `pickle.dumps()` - Serialize to bytes
- `pickle.loads()` - Deserialize from bytes

### json Module
JSON serialization.

**Functions:**
- `json.dump()` - Write JSON to file
- `json.load()` - Read JSON from file
- `json.dumps()` - Convert to JSON string
- `json.loads()` - Parse JSON string

### csv Module
CSV file handling.

**Functions:**
- `csv.reader()` - Read CSV
- `csv.writer()` - Write CSV
- `csv.DictReader()` - Read as dictionary
- `csv.DictWriter()` - Write from dictionary

## Best Practices

1. Use comprehensions for simple transformations
2. Prefer generators for large datasets
3. Use context managers for resource management
4. Apply decorators for cross-cutting concerns
5. Understand when to use threading vs multiprocessing
6. Use `functools.wraps` in decorators
7. Be careful with circular references
8. Use appropriate serialization format
9. Learn regular expressions for text processing
10. Understand iterator protocol for custom iterables

