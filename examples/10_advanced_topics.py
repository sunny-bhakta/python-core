"""
Advanced Topics Examples
=========================
This file demonstrates comprehensions, generators, iterators, decorators, and more.
"""

# ============================================================================
# COMPREHENSIONS
# ============================================================================

print("=" * 60)
print("COMPREHENSIONS")
print("=" * 60)

# List comprehensions
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Nested list comprehensions
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Dictionary comprehensions
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")

filtered_dict = {k: v for k, v in squares_dict.items() if v > 5}
print(f"Filtered dict: {filtered_dict}")

# Set comprehensions
unique_squares = {x**2 for x in range(-5, 6)}
print(f"Unique squares: {unique_squares}")

# Generator expressions (lazy evaluation)
squares_gen = (x**2 for x in range(10))
print(f"Generator: {squares_gen}")
print(f"First 5: {[next(squares_gen) for _ in range(5)]}")

# ============================================================================
# GENERATORS
# ============================================================================

print("\n" + "=" * 60)
print("GENERATORS")
print("=" * 60)

# Generator function
def countdown(n):
    """Countdown generator"""
    while n > 0:
        yield n
        n -= 1

print("Countdown:")
for num in countdown(5):
    print(f"  {num}")

# Fibonacci generator
def fibonacci():
    """Infinite Fibonacci generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print("\nFirst 10 Fibonacci numbers:")
for i in range(10):
    print(f"  {next(fib)}")

# Generator with send()
def accumulator():
    """Generator that accumulates values"""
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

acc = accumulator()
next(acc)  # Prime the generator
print(f"\nAccumulator: {acc.send(10)}")
print(f"Accumulator: {acc.send(5)}")
print(f"Accumulator: {acc.send(3)}")

# Generator pipeline
def numbers():
    """Generate numbers"""
    for i in range(10):
        yield i

def square(gen):
    """Square generator"""
    for num in gen:
        yield num ** 2

def filter_even(gen):
    """Filter even numbers"""
    for num in gen:
        if num % 2 == 0:
            yield num

pipeline = filter_even(square(numbers()))
print(f"\nPipeline result: {list(pipeline)}")

# ============================================================================
# ITERATORS
# ============================================================================

print("\n" + "=" * 60)
print("ITERATORS")
print("=" * 60)

# Built-in iterators
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
print(f"First: {next(iterator)}")
print(f"Second: {next(iterator)}")
print(f"Third: {next(iterator)}")

# Custom iterator
class CountUpTo:
    """Custom iterator that counts up to n"""
    
    def __init__(self, n):
        self.n = n
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current
        raise StopIteration

counter = CountUpTo(5)
print("\nCustom iterator:")
for num in counter:
    print(f"  {num}")

# Iterator with iter() function
text = "Python"
text_iter = iter(text)
print(f"\nString iterator: {list(text_iter)}")

# ============================================================================
# CONTEXT MANAGERS
# ============================================================================

print("\n" + "=" * 60)
print("CONTEXT MANAGERS")
print("=" * 60)

# Class-based context manager
class Timer:
    """Context manager for timing code"""
    
    def __init__(self):
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        import time
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        print(f"  Elapsed time: {elapsed:.4f} seconds")
        return False

with Timer():
    sum(range(1000000))

# Function-based context manager
from contextlib import contextmanager

@contextmanager
def temporary_change(obj, attr, value):
    """Temporarily change an attribute"""
    old_value = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, old_value)

class MyClass:
    def __init__(self):
        self.value = 10

obj = MyClass()
print(f"\nOriginal value: {obj.value}")
with temporary_change(obj, 'value', 20):
    print(f"  Temporary value: {obj.value}")
print(f"Restored value: {obj.value}")

# ============================================================================
# DECORATORS
# ============================================================================

print("\n" + "=" * 60)
print("DECORATORS")
print("=" * 60)

# Simple decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"  Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  {func.__name__} finished")
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("  Hello!")

say_hello()

# Timing decorator with functools.wraps
from functools import wraps
import time

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(0.1)
    return "Done"

slow_function()

# Caching decorator
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci_cached(n):
    """Fibonacci with caching"""
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

print(f"\nFibonacci(30) with caching: {fibonacci_cached(30)}")

# ============================================================================
# CLOSURES
# ============================================================================

print("\n" + "=" * 60)
print("CLOSURES")
print("=" * 60)

# Simple closure
def outer_function(x):
    """Outer function"""
    def inner_function(y):
        """Inner function (closure)"""
        return x + y
    return inner_function

add_five = outer_function(5)
print(f"add_five(10) = {add_five(10)}")
print(f"add_five(20) = {add_five(20)}")

# Closure with mutable variable
def counter():
    """Counter using closure"""
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter1 = counter()
counter2 = counter()

print(f"\nCounter 1: {counter1()}, {counter1()}, {counter1()}")
print(f"Counter 2: {counter2()}, {counter2()}")

# ============================================================================
# METACLASSES
# ============================================================================

print("\n" + "=" * 60)
print("METACLASSES")
print("=" * 60)

# Using type() to create class dynamically
MyClass = type('MyClass', (), {'x': 10, 'y': 20})
obj = MyClass()
print(f"Dynamic class: x={obj.x}, y={obj.y}")

# Custom metaclass
class Meta(type):
    """Custom metaclass"""
    def __new__(cls, name, bases, dct):
        dct['created_by'] = 'Meta'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
print(f"Class created by metaclass: {obj.created_by}")

# ============================================================================
# DESCRIPTORS
# ============================================================================

print("\n" + "=" * 60)
print("DESCRIPTORS")
print("=" * 60)

# Descriptor class
class Descriptor:
    """Simple descriptor"""
    
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        return f"Getting {self.name}"
    
    def __set__(self, obj, value):
        print(f"Setting {self.name} to {value}")

class MyClass:
    attr = Descriptor("attr")

obj = MyClass()
print(f"  {obj.attr}")
obj.attr = "new value"

# ============================================================================
# MEMORY MANAGEMENT
# ============================================================================

print("\n" + "=" * 60)
print("MEMORY MANAGEMENT")
print("=" * 60)

import gc
import sys

# Reference counting
x = [1, 2, 3]
print(f"Reference count: {sys.getrefcount(x)}")

# Garbage collection
print(f"GC counts: {gc.get_count()}")
gc.collect()
print(f"After collection: {gc.get_count()}")

# Circular reference
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1  # Circular reference

print(f"Circular reference created")
print(f"GC can collect: {gc.isenabled()}")

# ============================================================================
# REGULAR EXPRESSIONS
# ============================================================================

print("\n" + "=" * 60)
print("REGULAR EXPRESSIONS")
print("=" * 60)

import re

# Search
text = "The quick brown fox jumps over the lazy dog"
match = re.search(r'fox', text)
if match:
    print(f"Found 'fox' at position {match.start()}")

# Find all
numbers = re.findall(r'\d+', "I have 3 apples and 5 oranges")
print(f"Numbers found: {numbers}")

# Substitution
new_text = re.sub(r'\d+', 'X', "I have 3 apples and 5 oranges")
print(f"After substitution: {new_text}")

# Pattern groups
pattern = r'(\d{3})-(\d{3})-(\d{4})'
phone = "123-456-7890"
match = re.match(pattern, phone)
if match:
    print(f"Phone: {match.group(0)}")
    print(f"Area code: {match.group(1)}")

# Compiled pattern
pattern = re.compile(r'\d+')
matches = pattern.findall("3 apples, 5 oranges")
print(f"Compiled pattern matches: {matches}")

# ============================================================================
# SERIALIZATION
# ============================================================================

print("\n" + "=" * 60)
print("SERIALIZATION")
print("=" * 60)

# JSON
import json

data = {"name": "Alice", "age": 30, "city": "NYC"}
json_str = json.dumps(data)
print(f"JSON string: {json_str}")

parsed = json.loads(json_str)
print(f"Parsed back: {parsed}")

# Pickle
import pickle

data = [1, 2, 3, {"key": "value"}]
pickled = pickle.dumps(data)
print(f"Pickled size: {len(pickled)} bytes")

unpickled = pickle.loads(pickled)
print(f"Unpickled: {unpickled}")

# CSV
import csv
import io

csv_data = "Name,Age,City\nAlice,30,NYC\nBob,25,LA"
reader = csv.DictReader(io.StringIO(csv_data))
print("\nCSV data:")
for row in reader:
    print(f"  {row}")

