"""
Data Structures Examples
========================
This file demonstrates lists, tuples, dictionaries, and sets in Python.
"""

# ============================================================================
# LISTS
# ============================================================================

print("=" * 60)
print("LISTS")
print("=" * 60)

# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []
from_range = list(range(5))

print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print(f"From range: {from_range}")

# Accessing elements
print(f"\nFirst element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Slice [1:4]: {numbers[1:4]}")
print(f"Slice [::2]: {numbers[::2]}")  # Every other element
print(f"Reverse: {numbers[::-1]}")

# Modifying lists
numbers.append(6)
print(f"\nAfter append(6): {numbers}")

numbers.extend([7, 8])
print(f"After extend([7, 8]): {numbers}")

numbers.insert(0, 0)
print(f"After insert(0, 0): {numbers}")

numbers.remove(0)
print(f"After remove(0): {numbers}")

popped = numbers.pop()
print(f"After pop(): {numbers}, popped: {popped}")

popped_at_index = numbers.pop(2)
print(f"After pop(2): {numbers}, popped: {popped_at_index}")

# List methods
print(f"\nLength: {len(numbers)}")
print(f"Count of 3: {numbers.count(3)}")
print(f"Index of 3: {numbers.index(3)}")
print(f"Is 5 in list: {5 in numbers}")

# Sorting
unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
unsorted.sort()
print(f"\nSorted: {unsorted}")

unsorted.reverse()
print(f"Reversed: {unsorted}")

# List comprehensions
squares = [x**2 for x in range(10)]
print(f"\nSquares 0-9: {squares}")

evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers 0-19: {evens}")

nested = [[x*y for y in range(3)] for x in range(3)]
print(f"Nested list: {nested}")

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nMatrix: {matrix}")
print(f"Element [1][2]: {matrix[1][2]}")

# ============================================================================
# TUPLES
# ============================================================================

print("\n" + "=" * 60)
print("TUPLES")
print("=" * 60)

# Creating tuples
my_tuple = (1, 2, 3)
single_item = (42,)  # Note comma required
mixed_tuple = (1, "hello", 3.14)
from_list = tuple([1, 2, 3])

print(f"Tuple: {my_tuple}")
print(f"Single item: {single_item}")
print(f"Mixed: {mixed_tuple}")

# Accessing (same as lists)
print(f"\nFirst element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")
print(f"Slice [1:]: {my_tuple[1:]}")

# Tuple unpacking
a, b, c = my_tuple
print(f"\nUnpacked: a={a}, b={b}, c={c}")

# Swapping values
x, y = 10, 20
print(f"Before swap: x={x}, y={y}")
x, y = y, x
print(f"After swap: x={x}, y={y}")

# Multiple return values
def get_name_age():
    return "Alice", 30

name, age = get_name_age()
print(f"\nFunction returns: name={name}, age={age}")

# Named tuples
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
p2 = Point(3, 4)

print(f"\nPoint 1: x={p1.x}, y={p1.y}")
print(f"Point 2: x={p2.x}, y={p2.y}")
print(f"Distance: {((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5}")

# Tuples as dictionary keys
locations = {
    (0, 0): "Origin",
    (1, 1): "Corner",
    (2, 2): "Diagonal"
}
print(f"\nDictionary with tuple keys: {locations}")

# ============================================================================
# DICTIONARIES
# ============================================================================

print("\n" + "=" * 60)
print("DICTIONARIES")
print("=" * 60)

# Creating dictionaries
person = {"name": "Alice", "age": 30, "city": "NYC"}
empty_dict = {}
from_pairs = dict([("a", 1), ("b", 2), ("c", 3)])

print(f"Person: {person}")
print(f"From pairs: {from_pairs}")

# Accessing values
print(f"\nName: {person['name']}")
print(f"Age: {person.get('age')}")
print(f"Country: {person.get('country', 'Unknown')}")  # Default value

# All keys, values, items
print(f"\nKeys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Modifying dictionaries
person["email"] = "alice@example.com"
print(f"\nAfter adding email: {person}")

person.update({"age": 31, "phone": "123-456-7890"})
print(f"After update: {person}")

removed = person.pop("phone")
print(f"After pop('phone'): {person}, removed: {removed}")

# Dictionary comprehensions
squares_dict = {x: x**2 for x in range(5)}
print(f"\nSquares dict: {squares_dict}")

filtered = {k: v for k, v in person.items() if isinstance(v, str)}
print(f"Filtered (strings only): {filtered}")

# Nested dictionaries
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 21, "grade": "B"},
    "Charlie": {"age": 19, "grade": "A"}
}
print(f"\nNested dict: {students}")
print(f"Alice's grade: {students['Alice']['grade']}")

# Default dictionaries
from collections import defaultdict

word_count = defaultdict(int)
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    word_count[word] += 1
print(f"\nWord count: {dict(word_count)}")

# ============================================================================
# SETS
# ============================================================================

print("\n" + "=" * 60)
print("SETS")
print("=" * 60)

# Creating sets
my_set = {1, 2, 3, 4, 5}
empty_set = set()  # Not {} (that's a dict)
from_list = set([1, 2, 2, 3, 3, 3])  # Duplicates removed

print(f"Set: {my_set}")
print(f"From list (duplicates removed): {from_list}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")

print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print(f"Symmetric difference: {set1 ^ set2}")

# Set methods
set1.add(6)
print(f"\nAfter add(6): {set1}")

set1.discard(6)
print(f"After discard(6): {set1}")

set1.remove(5)
print(f"After remove(5): {set1}")

# Set comprehensions
evens_set = {x for x in range(20) if x % 2 == 0}
print(f"\nEven numbers set: {evens_set}")

# Frozen sets (immutable)
frozen = frozenset([1, 2, 3, 4, 5])
print(f"\nFrozen set: {frozen}")
# frozen.add(6)  # This would raise an error

# Using sets for unique elements
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(numbers_with_duplicates))
print(f"\nUnique from {numbers_with_duplicates}: {unique}")

# ============================================================================
# STRINGS AS SEQUENCES
# ============================================================================

print("\n" + "=" * 60)
print("STRINGS AS SEQUENCES")
print("=" * 60)

text = "Python"

# Indexing and slicing (same as lists)
print(f"Text: {text}")
print(f"First char: {text[0]}")
print(f"Last char: {text[-1]}")
print(f"Slice [1:4]: {text[1:4]}")
print(f"Reverse: {text[::-1]}")

# Iteration
print("\nCharacters:")
for char in text:
    print(f"  {char}")

# Membership
print(f"\n'P' in text: {'P' in text}")
print(f"'thon' in text: {'thon' in text}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Counting occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word count: {word_count}")

# Example 2: Finding common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"Common elements: {common}")

# Example 3: Grouping data
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "David", "grade": "C"}
]

grades_dict = {}
for student in students:
    grade = student["grade"]
    if grade not in grades_dict:
        grades_dict[grade] = []
    grades_dict[grade].append(student["name"])

print(f"Students by grade: {grades_dict}")

# Example 4: Matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"Original: {matrix}")
print(f"Transposed: {transposed}")

