"""
Functions Examples
==================
This file demonstrates all aspects of functions in Python.
"""

# ============================================================================
# BASIC FUNCTION DEFINITION
# ============================================================================

print("=" * 60)
print("BASIC FUNCTION DEFINITION")
print("=" * 60)

def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with multiple parameters
def add(a, b):
    """Adds two numbers"""
    return a + b

print(f"5 + 3 = {add(5, 3)}")

# Function without return (returns None)
def print_message(msg):
    """Prints a message"""
    print(f"Message: {msg}")

result = print_message("Hello")
print(f"Function without return: {result}")

# ============================================================================
# FUNCTION PARAMETERS
# ============================================================================

print("\n" + "=" * 60)
print("FUNCTION PARAMETERS")
print("=" * 60)

# Positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"I have a {animal_type} named {pet_name}")

describe_pet("dog", "Willie")
describe_pet("cat", "Fluffy")

# Keyword arguments
describe_pet(pet_name="Willie", animal_type="dog")
describe_pet(animal_type="cat", pet_name="Fluffy")

# Mixing positional and keyword
describe_pet("dog", pet_name="Willie")

# Default parameters
def greet_person(name, greeting="Hello", punctuation="!"):
    """Greet a person with optional greeting and punctuation"""
    return f"{greeting}, {name}{punctuation}"

print(greet_person("Alice"))
print(greet_person("Bob", "Hi"))
print(greet_person("Charlie", "Hey", "?"))

# Important: Mutable default arguments (common pitfall)
def add_item(item, items=[]):  # Wrong!
    items.append(item)
    return items

# Correct way
def add_item_correct(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print("\nMutable default argument issue:")
print(f"First call: {add_item('a')}")
print(f"Second call: {add_item('b')}")  # Unexpected!

print("\nCorrect implementation:")
print(f"First call: {add_item_correct('a')}")
print(f"Second call: {add_item_correct('b')}")

# *args - variable positional arguments
def sum_all(*args):
    """Sum all arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(f"\nSum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")
print(f"Sum of 10, 20: {sum_all(10, 20)}")

def make_sandwich(*toppings):
    """Make a sandwich with various toppings"""
    print("Making sandwich with:")
    for topping in toppings:
        print(f"  - {topping}")

make_sandwich("ham", "cheese", "lettuce")

# **kwargs - variable keyword arguments
def build_profile(**kwargs):
    """Build a user profile from keyword arguments"""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

user = build_profile(first_name="Alice", last_name="Smith", age=30, city="NYC")
print(f"\nUser profile: {user}")

# Combining parameter types
def complex_function(pos1, pos2, *args, kw1, kw2="default", **kwargs):
    """Function with all parameter types"""
    print(f"Positional: {pos1}, {pos2}")
    print(f"*args: {args}")
    print(f"Keyword: kw1={kw1}, kw2={kw2}")
    print(f"**kwargs: {kwargs}")

complex_function(1, 2, 3, 4, 5, kw1="required", extra="value", another=42)

# ============================================================================
# RETURN VALUES
# ============================================================================

print("\n" + "=" * 60)
print("RETURN VALUES")
print("=" * 60)

# Single return value
def square(x):
    return x ** 2

print(f"Square of 5: {square(5)}")

# Multiple return values (returns tuple)
def get_name_age():
    return "Alice", 30

name, age = get_name_age()
print(f"Name: {name}, Age: {age}")

# Unpacking return values
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)
print(f"17 divided by 5: quotient={q}, remainder={r}")

# Early return
def find_first_even(numbers):
    """Find first even number, return None if not found"""
    for num in numbers:
        if num % 2 == 0:
            return num
    return None

print(f"First even in [1, 3, 5, 8, 9]: {find_first_even([1, 3, 5, 8, 9])}")
print(f"First even in [1, 3, 5]: {find_first_even([1, 3, 5])}")

# ============================================================================
# LAMBDA FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("LAMBDA FUNCTIONS")
print("=" * 60)

# Basic lambda
square_lambda = lambda x: x ** 2
print(f"Square of 5 (lambda): {square_lambda(5)}")

# Lambda with multiple parameters
add_lambda = lambda a, b: a + b
print(f"5 + 3 (lambda): {add_lambda(5, 3)}")

# Lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared {numbers}: {squared}")

# Lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers in {numbers}: {evens}")

# Lambda with sorted()
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_by_age = sorted(people, key=lambda x: x[1])
print(f"Sorted by age: {sorted_by_age}")

# ============================================================================
# RECURSIVE FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("RECURSIVE FUNCTIONS")
print("=" * 60)

# Factorial
def factorial(n):
    """Calculate factorial recursively"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# Fibonacci
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci(7): {fibonacci(7)}")
print("First 10 Fibonacci numbers:")
for i in range(10):
    print(f"  F({i}) = {fibonacci(i)}")

# Recursive list sum
def recursive_sum(numbers):
    """Sum list recursively"""
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

print(f"\nSum of [1, 2, 3, 4, 5]: {recursive_sum([1, 2, 3, 4, 5])}")

# ============================================================================
# HIGHER-ORDER FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("HIGHER-ORDER FUNCTIONS")
print("=" * 60)

# map() - apply function to all items
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled {numbers}: {doubled}")

# filter() - filter items based on condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers in {numbers}: {evens}")

# reduce() - reduce sequence to single value
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of {numbers}: {product}")

# Function that returns a function
def make_multiplier(n):
    """Return a function that multiplies by n"""
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(f"Double of 5: {double(5)}")
print(f"Triple of 5: {triple(5)}")

# ============================================================================
# GENERATOR FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("GENERATOR FUNCTIONS")
print("=" * 60)

def countdown(n):
    """Generator that counts down from n"""
    while n > 0:
        yield n
        n -= 1

print("Countdown from 5:")
for num in countdown(5):
    print(f"  {num}")

def fibonacci_generator():
    """Generator for Fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
print("\nFirst 10 Fibonacci numbers (generator):")
for i in range(10):
    print(f"  {next(fib)}")

def squares(n):
    """Generator for squares up to n"""
    for i in range(1, n + 1):
        yield i ** 2

print(f"\nSquares up to 5: {list(squares(5))}")

# ============================================================================
# FUNCTION SCOPE
# ============================================================================

print("\n" + "=" * 60)
print("FUNCTION SCOPE")
print("=" * 60)

# Local scope
x = "global"

def local_scope():
    x = "local"
    print(f"Inside function: x = {x}")

local_scope()
print(f"Outside function: x = {x}")

# Global scope
counter = 0

def increment():
    global counter
    counter += 1
    print(f"Counter: {counter}")

increment()
increment()
print(f"Final counter: {counter}")

# Nonlocal scope
def outer():
    x = "outer"
    
    def inner():
        nonlocal x
        x = "inner"
        print(f"Inner: x = {x}")
    
    print(f"Before inner: x = {x}")
    inner()
    print(f"After inner: x = {x}")

outer()

# Closures
def make_counter():
    """Create a counter function using closure"""
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter1 = make_counter()
counter2 = make_counter()

print(f"\nCounter 1: {counter1()}, {counter1()}, {counter1()}")
print(f"Counter 2: {counter2()}, {counter2()}")

# ============================================================================
# DECORATORS
# ============================================================================

print("\n" + "=" * 60)
print("DECORATORS")
print("=" * 60)

# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Something before function")
        func()
        print("Something after function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Timing decorator
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(0.1)
    return "Done"

slow_function()

# ============================================================================
# DOCSTRINGS
# ============================================================================

print("\n" + "=" * 60)
print("DOCSTRINGS")
print("=" * 60)

def documented_function(param1, param2):
    """
    This is a documented function.
    
    Args:
        param1: First parameter description
        param2: Second parameter description
    
    Returns:
        Description of return value
    """
    return param1 + param2

print("Function docstring:")
print(documented_function.__doc__)

# Accessing docstring
help(documented_function)

