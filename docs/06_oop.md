# Object-Oriented Programming

## Overview
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects" that contain data (attributes) and code (methods).

## Classes & Objects

### Class Definition

```python
class ClassName:
    """Class docstring"""
    # Class body
```

### Object Instantiation

```python
object_name = ClassName()
```

### Instance Variables
Variables unique to each instance.

### Class Variables
Variables shared by all instances.

### Methods

**Instance Methods:**
- First parameter is `self`
- Access instance variables and methods
- Called on instance: `object.method()`

**Class Methods:**
- Decorated with `@classmethod`
- First parameter is `cls`
- Can access class variables
- Called on class: `ClassName.method()`

**Static Methods:**
- Decorated with `@staticmethod`
- No `self` or `cls` parameter
- Cannot access instance or class variables
- Called on class or instance

## Special Methods (Magic/Dunder Methods)

Special methods that define behavior for built-in operations.

**Common Special Methods:**
- `__init__(self, ...)` - Constructor
- `__str__(self)` - String representation (user-friendly)
- `__repr__(self)` - String representation (developer-friendly)
- `__len__(self)` - Length
- `__getitem__(self, key)` - Indexing
- `__setitem__(self, key, value)` - Assignment
- `__delitem__(self, key)` - Deletion
- `__eq__(self, other)` - Equality (`==`)
- `__lt__(self, other)` - Less than (`<`)
- `__gt__(self, other)` - Greater than (`>`)
- `__add__(self, other)` - Addition (`+`)
- `__sub__(self, other)` - Subtraction (`-`)
- `__mul__(self, other)` - Multiplication (`*`)

## Inheritance

### Single Inheritance

```python
class ChildClass(ParentClass):
    pass
```

### Multiple Inheritance

```python
class ChildClass(Parent1, Parent2):
    pass
```

### Method Resolution Order (MRO)
Determines order of method lookup in inheritance hierarchy.

### super() Function
Calls method from parent class.

### Method Overriding
Child class redefines parent class method.

## Encapsulation

### Access Modifiers

**Public:**
- No prefix
- Accessible everywhere

**Protected:**
- Single underscore prefix: `_variable`
- Convention only (still accessible)

**Private:**
- Double underscore prefix: `__variable`
- Name mangling: `_ClassName__variable`

### Property Decorators

```python
@property
def attribute(self):
    return self._attribute

@attribute.setter
def attribute(self, value):
    self._attribute = value

@attribute.deleter
def attribute(self):
    del self._attribute
```

## Polymorphism

### Duck Typing
"If it walks like a duck and quacks like a duck, it's a duck."

Python uses duck typing - objects are used based on their behavior, not their type.

### Method Overriding
Different classes can implement same method differently.

### Operator Overloading
Using special methods to define behavior for operators.

## Abstract Classes

### abc Module

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def method(self):
        pass
```

Abstract methods must be implemented by subclasses.

## Best Practices

1. Use meaningful class and method names
2. Follow single responsibility principle
3. Use composition over inheritance when appropriate
4. Prefer composition for "has-a" relationships
5. Use inheritance for "is-a" relationships
6. Use `super()` for parent class calls
7. Document classes and methods with docstrings
8. Use properties for computed attributes
9. Keep classes focused and cohesive
10. Follow naming conventions (PascalCase for classes)

