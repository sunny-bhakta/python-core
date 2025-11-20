# Data Structures

## Overview
Python provides several built-in data structures for organizing and storing data. Each has specific use cases and characteristics.

## Lists (`list`)

### Characteristics
- **Ordered**: Maintains insertion order
- **Mutable**: Can be modified after creation
- **Indexed**: Access elements by index (0-based)
- **Heterogeneous**: Can contain different types
- **Dynamic**: Size can change

### Common Operations

**Creation:**
```python
my_list = [1, 2, 3]
empty_list = []
list_from_range = list(range(5))
```

**Accessing:**
- Indexing: `list[index]`
- Slicing: `list[start:stop:step]`
- Negative indexing: `list[-1]` (last element)

**Modification:**
- `append(item)` - Add to end
- `extend(iterable)` - Add multiple items
- `insert(index, item)` - Insert at position
- `remove(item)` - Remove first occurrence
- `pop(index)` - Remove and return item
- `clear()` - Remove all items

**Information:**
- `len(list)` - Length
- `count(item)` - Count occurrences
- `index(item)` - Find index
- `in` operator - Check membership

**Sorting:**
- `sort()` - Sort in place
- `reverse()` - Reverse in place
- `sorted(list)` - Return sorted copy

**List Comprehensions:**
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

## Tuples (`tuple`)

### Characteristics
- **Ordered**: Maintains insertion order
- **Immutable**: Cannot be modified after creation
- **Indexed**: Access elements by index
- **Heterogeneous**: Can contain different types
- **Hashable**: Can be used as dictionary keys

### Common Operations

**Creation:**
```python
my_tuple = (1, 2, 3)
single_item = (42,)  # Note the comma
tuple_from_list = tuple([1, 2, 3])
```

**Accessing:**
- Same as lists (indexing, slicing)
- Cannot modify elements

**Tuple Unpacking:**
```python
a, b, c = (1, 2, 3)
x, y = y, x  # Swap values
```

**Named Tuples:**
```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
```

## Dictionaries (`dict`)

### Characteristics
- **Unordered** (Python 3.7+: insertion order preserved)
- **Mutable**: Can be modified
- **Key-Value pairs**: Access by key, not index
- **Keys must be hashable**: Strings, numbers, tuples
- **No duplicate keys**: Later values overwrite earlier

### Common Operations

**Creation:**
```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
empty_dict = {}
dict_from_pairs = dict([('a', 1), ('b', 2)])
```

**Accessing:**
- `dict[key]` - Get value (raises KeyError if missing)
- `dict.get(key, default)` - Get with default
- `dict.keys()` - All keys
- `dict.values()` - All values
- `dict.items()` - All key-value pairs

**Modification:**
- `dict[key] = value` - Add/update
- `update(other_dict)` - Merge dictionaries
- `pop(key, default)` - Remove and return
- `popitem()` - Remove last item (3.7+)
- `clear()` - Remove all

**Dictionary Comprehensions:**
```python
squares = {x: x**2 for x in range(5)}
filtered = {k: v for k, v in dict.items() if v > 0}
```

## Sets (`set`)

### Characteristics
- **Unordered**: No guaranteed order
- **Mutable**: Can be modified
- **Unique elements**: No duplicates
- **Hashable elements**: Elements must be immutable
- **Fast membership testing**: O(1) average case

### Common Operations

**Creation:**
```python
my_set = {1, 2, 3}
empty_set = set()  # Not {} (that's a dict)
set_from_list = set([1, 2, 3])
```

**Modification:**
- `add(item)` - Add element
- `remove(item)` - Remove (raises KeyError if missing)
- `discard(item)` - Remove (no error if missing)
- `pop()` - Remove and return arbitrary element
- `clear()` - Remove all

**Set Operations:**
- Union: `set1 | set2` or `set1.union(set2)`
- Intersection: `set1 & set2` or `set1.intersection(set2)`
- Difference: `set1 - set2` or `set1.difference(set2)`
- Symmetric Difference: `set1 ^ set2` or `set1.symmetric_difference(set2)`

**Set Comprehensions:**
```python
evens = {x for x in range(10) if x % 2 == 0}
```

**Frozen Sets:**
- Immutable sets: `frozenset([1, 2, 3])`
- Can be used as dictionary keys

## Strings (as Sequences)

Strings share many operations with lists and tuples.

**Common Operations:**
- Indexing and slicing
- `len(string)`
- `in` operator
- Iteration with `for`
- String methods (see Basic Syntax section)

## Choosing the Right Data Structure

**Use Lists when:**
- Order matters
- Need to modify elements
- Need duplicates
- Sequential access

**Use Tuples when:**
- Data shouldn't change
- Need hashable collection
- Returning multiple values from function
- Dictionary keys

**Use Dictionaries when:**
- Need key-value mapping
- Fast lookups by key
- Associating data

**Use Sets when:**
- Need unique elements
- Fast membership testing
- Set operations (union, intersection, etc.)
- Removing duplicates

## Best Practices

1. Use list comprehensions for simple transformations
2. Prefer tuples for immutable data
3. Use `.get()` for safe dictionary access
4. Use sets for membership testing
5. Consider `collections` module for specialized needs
6. Use appropriate data structure for the task
7. Be aware of mutability vs immutability
8. Understand time complexity of operations

