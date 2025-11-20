"""
Standard Library Examples
==========================
This file demonstrates essential standard library modules in Python.
"""

# ============================================================================
# os MODULE
# ============================================================================

print("=" * 60)
print("os MODULE")
print("=" * 60)

import os

print(f"Current directory: {os.getcwd()}")
print(f"OS name: {os.name}")
print(f"Environment variable HOME: {os.environ.get('HOME', 'N/A')}")

# List directory
print(f"\nFiles in current directory (first 5):")
files = os.listdir('.')[:5]
for f in files:
    print(f"  {f}")

# Path operations
file_path = os.path.join('docs', 'example.txt')
print(f"\nJoined path: {file_path}")
print(f"Directory: {os.path.dirname(file_path)}")
print(f"Basename: {os.path.basename(file_path)}")
print(f"Exists: {os.path.exists('README.md')}")

# ============================================================================
# sys MODULE
# ============================================================================

print("\n" + "=" * 60)
print("sys MODULE")
print("=" * 60)

import sys

print(f"Python version: {sys.version.split()[0]}")
print(f"Platform: {sys.platform}")
print(f"Executable: {sys.executable}")
print(f"Module search path (first 3):")
for path in sys.path[:3]:
    print(f"  {path}")

# ============================================================================
# math MODULE
# ============================================================================

print("\n" + "=" * 60)
print("math MODULE")
print("=" * 60)

import math

print(f"Pi: {math.pi}")
print(f"E: {math.e}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"2^3: {math.pow(2, 3)}")
print(f"Sin(pi/2): {math.sin(math.pi/2)}")
print(f"Log(e): {math.log(math.e)}")
print(f"Ceil(4.3): {math.ceil(4.3)}")
print(f"Floor(4.7): {math.floor(4.7)}")
print(f"Factorial(5): {math.factorial(5)}")

# ============================================================================
# random MODULE
# ============================================================================

print("\n" + "=" * 60)
print("random MODULE")
print("=" * 60)

import random

print(f"Random float [0,1): {random.random()}")
print(f"Random int [1,10]: {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['apple', 'banana', 'cherry'])}")

numbers = [1, 2, 3, 4, 5]
shuffled = numbers.copy()
random.shuffle(shuffled)
print(f"Shuffled {numbers}: {shuffled}")
print(f"Random sample (3): {random.sample(numbers, 3)}")

# ============================================================================
# datetime MODULE
# ============================================================================

print("\n" + "=" * 60)
print("datetime MODULE")
print("=" * 60)

from datetime import datetime, date, time, timedelta

now = datetime.now()
print(f"Current datetime: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

today = date.today()
print(f"Today: {today}")

current_time = time(14, 30, 45)
print(f"Time: {current_time}")

# Timedelta
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
print(f"Tomorrow: {tomorrow}")
print(f"Next week: {next_week}")

# Parsing
parsed = datetime.strptime("2024-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")
print(f"Parsed: {parsed}")

# ============================================================================
# json MODULE
# ============================================================================

print("\n" + "=" * 60)
print("json MODULE")
print("=" * 60)

import json

# Python to JSON
data = {
    "name": "Alice",
    "age": 30,
    "city": "NYC",
    "hobbies": ["reading", "coding"]
}
json_str = json.dumps(data, indent=2)
print("JSON string:")
print(json_str)

# JSON to Python
parsed = json.loads(json_str)
print(f"\nParsed back: {parsed}")

# File operations
with open("temp_data.json", 'w') as f:
    json.dump(data, f, indent=2)

with open("temp_data.json", 'r') as f:
    loaded = json.load(f)
    print(f"\nLoaded from file: {loaded}")

# Cleanup
os.remove("temp_data.json")

# ============================================================================
# csv MODULE
# ============================================================================

print("\n" + "=" * 60)
print("csv MODULE")
print("=" * 60)

import csv
import io

# Writing CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "NYC"],
    ["Bob", "25", "LA"],
    ["Charlie", "35", "Chicago"]
]

with open("temp_data.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Reading CSV
with open("temp_data.csv", 'r') as f:
    reader = csv.reader(f)
    print("CSV data:")
    for row in reader:
        print(f"  {row}")

# DictReader
with open("temp_data.csv", 'r') as f:
    reader = csv.DictReader(f)
    print("\nCSV as dictionaries:")
    for row in reader:
        print(f"  {row}")

# Cleanup
os.remove("temp_data.csv")

# ============================================================================
# re MODULE
# ============================================================================

print("\n" + "=" * 60)
print("re MODULE")
print("=" * 60)

import re

text = "Contact: email@example.com or call 123-456-7890"

# Search
email_match = re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
if email_match:
    print(f"Email found: {email_match.group()}")

# Find all
phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(f"Phone numbers: {phone_numbers}")

# Substitution
masked = re.sub(r'\d', 'X', "Phone: 123-456-7890")
print(f"Masked: {masked}")

# Groups
pattern = r'(\d{3})-(\d{3})-(\d{4})'
match = re.search(pattern, text)
if match:
    print(f"Full match: {match.group(0)}")
    print(f"Area code: {match.group(1)}")

# ============================================================================
# collections MODULE
# ============================================================================

print("\n" + "=" * 60)
print("collections MODULE")
print("=" * 60)

from collections import Counter, defaultdict, deque, namedtuple

# Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)
print(f"Word count: {counter}")
print(f"Most common: {counter.most_common(2)}")

# defaultdict
dd = defaultdict(int)
dd["a"] += 1
dd["b"] += 2
print(f"\nDefaultdict: {dict(dd)}")

# deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(f"\nDeque: {list(dq)}")
print(f"Pop left: {dq.popleft()}")
print(f"Pop right: {dq.pop()}")

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(f"\nNamed tuple: x={p.x}, y={p.y}")

# ============================================================================
# itertools MODULE
# ============================================================================

print("\n" + "=" * 60)
print("itertools MODULE")
print("=" * 60)

import itertools

# Count
print("Count (first 5):")
for i, num in enumerate(itertools.count(10)):
    if i >= 5:
        break
    print(f"  {num}")

# Cycle
print("\nCycle (first 5):")
for i, item in enumerate(itertools.cycle(['A', 'B', 'C'])):
    if i >= 5:
        break
    print(f"  {item}")

# Combinations
print("\nCombinations of [1,2,3,4] choose 2:")
for combo in itertools.combinations([1, 2, 3, 4], 2):
    print(f"  {combo}")

# Permutations
print("\nPermutations of [1,2,3] (first 3):")
for i, perm in enumerate(itertools.permutations([1, 2, 3])):
    if i >= 3:
        break
    print(f"  {perm}")

# Chain
print("\nChained iterables:")
for item in itertools.chain([1, 2], [3, 4], [5, 6]):
    print(f"  {item}")

# ============================================================================
# functools MODULE
# ============================================================================

print("\n" + "=" * 60)
print("functools MODULE")
print("=" * 60)

from functools import partial, reduce, lru_cache

# Partial
def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(f"Double of 5: {double(5)}")

# Reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of {numbers}: {product}")

# LRU Cache
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(30) with cache: {fibonacci(30)}")

# ============================================================================
# operator MODULE
# ============================================================================

print("\n" + "=" * 60)
print("operator MODULE")
print("=" * 60)

import operator

print(f"Add: {operator.add(3, 5)}")
print(f"Multiply: {operator.mul(3, 5)}")
print(f"Equal: {operator.eq(3, 3)}")

# Itemgetter
data = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
sorted_by_age = sorted(data, key=operator.itemgetter(1))
print(f"Sorted by age: {sorted_by_age}")

# ============================================================================
# logging MODULE
# ============================================================================

print("\n" + "=" * 60)
print("logging MODULE")
print("=" * 60)

import logging

# Basic configuration
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# ============================================================================
# pathlib MODULE
# ============================================================================

print("\n" + "=" * 60)
print("pathlib MODULE")
print("=" * 60)

from pathlib import Path

# Path operations
current = Path('.')
print(f"Current path: {current}")
print(f"Absolute: {current.absolute()}")

# File operations
test_file = Path("temp_test.txt")
test_file.write_text("Hello, Pathlib!")
content = test_file.read_text()
print(f"\nFile content: {content}")
print(f"Exists: {test_file.exists()}")
print(f"Is file: {test_file.is_file()}")

# Cleanup
test_file.unlink()

# ============================================================================
# typing MODULE
# ============================================================================

print("\n" + "=" * 60)
print("typing MODULE")
print("=" * 60)

from typing import List, Dict, Tuple, Optional, Union, Callable

# Type hints
def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def get_user(user_id: int) -> Optional[Dict[str, str]]:
    if user_id > 0:
        return {"id": str(user_id), "name": "Alice"}
    return None

def apply_func(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

result = process_numbers([1, 2, 3, 4, 5])
print(f"Sum: {result}")

user = get_user(1)
print(f"User: {user}")

add_result = apply_func(operator.add, 5, 3)
print(f"Applied function: {add_result}")

print("\nNote: Type hints are for documentation and static analysis")

