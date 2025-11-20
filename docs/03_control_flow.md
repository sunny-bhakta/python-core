# Control Flow

## Overview
Control flow statements allow you to control the execution order of your program. Python provides conditional statements and loops to manage program flow.

## Conditional Statements

### if, elif, else

The `if` statement allows conditional execution of code blocks.

**Syntax:**
```python
if condition1:
    # code block
elif condition2:
    # code block
else:
    # code block
```

**Key Points:**
- `if` is required
- `elif` (else if) is optional, can have multiple
- `else` is optional
- Conditions are evaluated in order
- First `True` condition executes, rest are skipped
- Indentation (4 spaces) defines code blocks

### Ternary Operators (Conditional Expressions)

Shorthand for simple if-else statements.

**Syntax:**
```python
value = true_value if condition else false_value
```

### Chained Comparisons

Python allows chaining comparison operators.

**Example:**
```python
if 1 < x < 10:  # Equivalent to: 1 < x and x < 10
    pass
```

## Loops

### for Loops

Iterate over sequences (lists, strings, tuples, etc.) or use `range()`.

**Syntax:**
```python
for item in sequence:
    # code block
```

**Key Features:**
- Automatically iterates through sequence
- Loop variable gets each item in sequence
- Can use `break` to exit early
- Can use `continue` to skip to next iteration
- Optional `else` clause executes if loop completes normally

### range() Function

Generates a sequence of numbers.

**Syntax:**
- `range(stop)` - 0 to stop-1
- `range(start, stop)` - start to stop-1
- `range(start, stop, step)` - start to stop-1 with step

**Characteristics:**
- Returns a range object (not a list)
- Memory efficient (generates values on demand)
- Can convert to list: `list(range(5))`

### enumerate()

Get both index and value when iterating.

**Syntax:**
```python
for index, value in enumerate(sequence):
    # code block
```

### zip()

Iterate over multiple sequences in parallel.

**Syntax:**
```python
for item1, item2 in zip(seq1, seq2):
    # code block
```

### while Loops

Execute code block while condition is `True`.

**Syntax:**
```python
while condition:
    # code block
```

**Key Points:**
- Condition checked before each iteration
- Must ensure condition becomes `False` eventually (avoid infinite loops)
- Can use `break` and `continue`
- Optional `else` clause executes if loop completes normally

## Loop Control

### break

Exits the innermost loop immediately.

**Use Cases:**
- Exit loop when condition met
- Search operations (found item, exit)
- Error conditions

### continue

Skips remaining code in current iteration, continues to next iteration.

**Use Cases:**
- Skip certain items
- Filter conditions
- Early iteration exit

### pass

Placeholder statement that does nothing.

**Use Cases:**
- Empty code blocks (syntax requires something)
- Placeholder for future code
- Minimal class/function definitions

### else Clause in Loops

The `else` clause executes when loop completes normally (not via `break`).

**Use Cases:**
- Search operations (not found case)
- Validation loops
- Cleanup code

## Nested Loops

Loops can be nested inside other loops.

**Common Patterns:**
- Iterating over 2D structures
- Generating combinations
- Matrix operations

## Best Practices

1. Use `for` loops when you know iteration count
2. Use `while` loops for conditional iteration
3. Prefer `enumerate()` over manual index tracking
4. Use `zip()` for parallel iteration
5. Be careful with infinite loops in `while`
6. Use meaningful loop variable names
7. Consider list comprehensions for simple transformations
8. Use `break` and `continue` judiciously for readability

