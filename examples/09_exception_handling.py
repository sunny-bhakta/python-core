"""
Exception Handling Examples
============================
This file demonstrates exception handling, raising exceptions, and custom exceptions.
"""

# ============================================================================
# BASIC EXCEPTION HANDLING
# ============================================================================

print("=" * 60)
print("BASIC EXCEPTION HANDLING")
print("=" * 60)

# try-except block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("  Caught ZeroDivisionError: Cannot divide by zero")

# Catching specific exception
try:
    value = int("not a number")
except ValueError:
    print("  Caught ValueError: Invalid integer conversion")

# Accessing exception information
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"  Exception details: {e}")
    print(f"  Exception type: {type(e).__name__}")

# ============================================================================
# MULTIPLE EXCEPTIONS
# ============================================================================

print("\n" + "=" * 60)
print("MULTIPLE EXCEPTIONS")
print("=" * 60)

# Catching multiple specific exceptions
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid types for division"

print(f"  10 / 2 = {divide_numbers(10, 2)}")
print(f"  10 / 0 = {divide_numbers(10, 0)}")
print(f"  10 / 'a' = {divide_numbers(10, 'a')}")

# Catching multiple exceptions in one clause
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"  Caught {type(e).__name__}: {e}")

# ============================================================================
# else CLAUSE
# ============================================================================

print("\n" + "=" * 60)
print("else CLAUSE")
print("=" * 60)

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  Division by zero!")
        return None
    else:
        print("  Division successful!")
        return result

print(f"  10 / 2: {safe_divide(10, 2)}")
print(f"  10 / 0: {safe_divide(10, 0)}")

# ============================================================================
# finally CLAUSE
# ============================================================================

print("\n" + "=" * 60)
print("finally CLAUSE")
print("=" * 60)

def file_operation(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"  File '{filename}' not found")
        return None
    finally:
        if file:
            file.close()
            print("  File closed in finally block")

file_operation("nonexistent.txt")

# ============================================================================
# COMMON EXCEPTION TYPES
# ============================================================================

print("\n" + "=" * 60)
print("COMMON EXCEPTION TYPES")
print("=" * 60)

# ValueError
try:
    int("abc")
except ValueError as e:
    print(f"  ValueError: {e}")

# TypeError
try:
    "hello" + 5
except TypeError as e:
    print(f"  TypeError: {e}")

# KeyError
try:
    d = {"key": "value"}
    value = d["nonexistent"]
except KeyError as e:
    print(f"  KeyError: {e}")

# IndexError
try:
    lst = [1, 2, 3]
    value = lst[10]
except IndexError as e:
    print(f"  IndexError: {e}")

# AttributeError
try:
    obj = None
    obj.some_method()
except AttributeError as e:
    print(f"  AttributeError: {e}")

# FileNotFoundError
try:
    with open("nonexistent.txt", 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"  FileNotFoundError: {e}")

# ============================================================================
# RAISING EXCEPTIONS
# ============================================================================

print("\n" + "=" * 60)
print("RAISING EXCEPTIONS")
print("=" * 60)

# Raise built-in exception
def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive")
    return number

try:
    check_positive(-5)
except ValueError as e:
    print(f"  Caught: {e}")

# Raise with message
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(f"  Caught: {e}")

# ============================================================================
# CUSTOM EXCEPTIONS
# ============================================================================

print("\n" + "=" * 60)
print("CUSTOM EXCEPTIONS")
print("=" * 60)

# Simple custom exception
class CustomError(Exception):
    """Custom exception class"""
    pass

# Custom exception with message
class ValidationError(Exception):
    """Custom validation error"""
    def __init__(self, message, value):
        self.message = message
        self.value = value
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}: {self.value}"

# Using custom exceptions
def validate_age(age):
    if age < 0:
        raise ValidationError("Age cannot be negative", age)
    if age > 150:
        raise ValidationError("Age seems unrealistic", age)
    return age

try:
    validate_age(-5)
except ValidationError as e:
    print(f"  Caught ValidationError: {e}")

try:
    validate_age(200)
except ValidationError as e:
    print(f"  Caught ValidationError: {e}")

# ============================================================================
# EXCEPTION CHAINING
# ============================================================================

print("\n" + "=" * 60)
print("EXCEPTION CHAINING")
print("=" * 60)

class ProcessingError(Exception):
    pass

def process_data(data):
    try:
        result = int(data)
    except ValueError as e:
        raise ProcessingError(f"Failed to process data: {data}") from e

try:
    process_data("invalid")
except ProcessingError as e:
    print(f"  Caught ProcessingError: {e}")
    print(f"  Original exception: {e.__cause__}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Safe dictionary access
def safe_get(dictionary, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default

data = {"name": "Alice", "age": 30}
print(f"  Safe get 'name': {safe_get(data, 'name')}")
print(f"  Safe get 'city': {safe_get(data, 'city', 'Unknown')}")

# Example 2: Input validation
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("  Invalid input. Please enter an integer.")
        except KeyboardInterrupt:
            print("\n  Input cancelled.")
            return None

# Example 3: File processing with error handling
def process_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"  File '{filename}' not found")
        return 0
    except PermissionError:
        print(f"  Permission denied for '{filename}'")
        return 0
    except Exception as e:
        print(f"  Unexpected error: {e}")
        return 0

# Example 4: Calculator with error handling
class Calculator:
    @staticmethod
    def divide(a, b):
        try:
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("Both arguments must be numbers")
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        except (TypeError, ZeroDivisionError) as e:
            print(f"  Calculator error: {e}")
            return None

calc = Calculator()
print(f"  10 / 2 = {calc.divide(10, 2)}")
print(f"  10 / 0 = {calc.divide(10, 0)}")
print(f"  '10' / 2 = {calc.divide('10', 2)}")

# ============================================================================
# EXCEPTION HIERARCHY
# ============================================================================

print("\n" + "=" * 60)
print("EXCEPTION HIERARCHY")
print("=" * 60)

# Check exception hierarchy
print("  Exception inheritance:")
print(f"    ValueError is subclass of Exception: {issubclass(ValueError, Exception)}")
print(f"    Exception is subclass of BaseException: {issubclass(Exception, BaseException)}")

# Catching base exception
try:
    int("abc")
except Exception as e:
    print(f"  Caught base Exception: {type(e).__name__}")

# Multiple levels
try:
    int("abc")
except ValueError:
    print("  Caught ValueError (specific)")
except Exception:
    print("  Caught Exception (general)")

