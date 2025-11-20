# Exception Handling

## Overview
Exception handling allows programs to gracefully handle errors and unexpected situations. Python uses try-except blocks to catch and handle exceptions.

## Exception Basics

### try-except Block

**Basic Syntax:**
```python
try:
    # Code that might raise exception
    pass
except ExceptionType:
    # Handle exception
    pass
```

### Exception Types

**Common Built-in Exceptions:**
- `Exception` - Base class for all exceptions
- `ValueError` - Invalid value
- `TypeError` - Wrong type
- `KeyError` - Dictionary key not found
- `IndexError` - List index out of range
- `FileNotFoundError` - File doesn't exist
- `ZeroDivisionError` - Division by zero
- `AttributeError` - Attribute doesn't exist
- `NameError` - Name not defined
- `SyntaxError` - Syntax error

### Catching Specific Exceptions

```python
try:
    # code
except ValueError:
    # Handle ValueError
except TypeError:
    # Handle TypeError
```

### Catching Multiple Exceptions

```python
try:
    # code
except (ValueError, TypeError):
    # Handle both
```

### else Clause

Executes if no exception occurs.

```python
try:
    # code
except Exception:
    # Handle exception
else:
    # Execute if no exception
```

### finally Clause

Always executes, regardless of exceptions.

```python
try:
    # code
except Exception:
    # Handle exception
finally:
    # Always executes
```

## Raising Exceptions

### raise Statement

```python
raise ValueError("Invalid value")
```

### Creating Custom Exceptions

```python
class CustomError(Exception):
    pass

class CustomErrorWithMessage(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
```

### Exception Chaining

```python
try:
    # code
except Exception as e:
    raise NewException("New error") from e
```

## Exception Hierarchy

All exceptions inherit from `BaseException`:
- `Exception` - User-defined exceptions
- `SystemExit` - System exit
- `KeyboardInterrupt` - Interrupt
- `GeneratorExit` - Generator exit

## Best Practices

1. Catch specific exceptions, not generic `Exception`
2. Use `else` for code that should run only if no exception
3. Use `finally` for cleanup code
4. Don't suppress exceptions silently
5. Provide meaningful error messages
6. Log exceptions appropriately
7. Create custom exceptions for domain-specific errors
8. Use exception chaining when appropriate
9. Clean up resources in `finally` blocks
10. Document exceptions that functions may raise

