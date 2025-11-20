# Variables & Operators

## Variables

### Variable Naming Rules

1. **Must start with a letter or underscore** (`_`)
2. **Can contain letters, digits, and underscores**
3. **Case-sensitive** (`name` and `Name` are different)
4. **Cannot use Python keywords** (if, for, def, etc.)
5. **Follow naming conventions**:
   - Use lowercase with underscores for variables: `my_variable`
   - Use UPPERCASE for constants: `MAX_SIZE`
   - Use PascalCase for classes: `MyClass`

### Dynamic Typing

Python uses dynamic typing, meaning:
- Variables don't need type declaration
- Type is determined at runtime
- Variables can be reassigned to different types

### Variable Scope

**Local Scope:**
- Variables defined inside a function
- Only accessible within that function

**Global Scope:**
- Variables defined at module level
- Accessible throughout the module
- Use `global` keyword to modify global variables inside functions

**Nonlocal Scope:**
- Variables in enclosing (non-global) scope
- Use `nonlocal` keyword to modify in nested functions

## Operators

### Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `3 + 2 = 5` |
| `-` | Subtraction | `3 - 2 = 1` |
| `*` | Multiplication | `3 * 2 = 6` |
| `/` | Division (float) | `3 / 2 = 1.5` |
| `//` | Floor division | `3 // 2 = 1` |
| `%` | Modulus (remainder) | `3 % 2 = 1` |
| `**` | Exponentiation | `3 ** 2 = 9` |

### Comparison Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal to | `3 == 3` → `True` |
| `!=` | Not equal to | `3 != 2` → `True` |
| `<` | Less than | `3 < 5` → `True` |
| `>` | Greater than | `3 > 5` → `False` |
| `<=` | Less than or equal | `3 <= 3` → `True` |
| `>=` | Greater than or equal | `3 >= 3` → `True` |

### Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | Logical AND | `True and False` → `False` |
| `or` | Logical OR | `True or False` → `True` |
| `not` | Logical NOT | `not True` → `False` |

**Short-circuit evaluation:**
- `and`: Stops at first `False`
- `or`: Stops at first `True`

### Assignment Operators

| Operator | Description | Equivalent To |
|----------|-------------|---------------|
| `=` | Assignment | `x = 5` |
| `+=` | Add and assign | `x += 3` → `x = x + 3` |
| `-=` | Subtract and assign | `x -= 3` → `x = x - 3` |
| `*=` | Multiply and assign | `x *= 3` → `x = x * 3` |
| `/=` | Divide and assign | `x /= 3` → `x = x / 3` |
| `//=` | Floor divide and assign | `x //= 3` → `x = x // 3` |
| `%=` | Modulus and assign | `x %= 3` → `x = x % 3` |
| `**=` | Exponentiate and assign | `x **= 3` → `x = x ** 3` |

### Identity Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `is` | Same object (identity) | `x is y` |
| `is not` | Not same object | `x is not y` |

**Note:** `is` checks identity (same object in memory), while `==` checks equality (same value).

### Membership Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `in` | Member of sequence | `'a' in 'abc'` → `True` |
| `not in` | Not member of sequence | `'d' in 'abc'` → `False` |

### Bitwise Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `&` | Bitwise AND | `5 & 3 = 1` |
| `\|` | Bitwise OR | `5 \| 3 = 7` |
| `^` | Bitwise XOR | `5 ^ 3 = 6` |
| `~` | Bitwise NOT | `~5 = -6` |
| `<<` | Left shift | `5 << 1 = 10` |
| `>>` | Right shift | `5 >> 1 = 2` |

### Operator Precedence

Operators are evaluated in this order (highest to lowest):

1. Parentheses `()`
2. Exponentiation `**`
3. Unary `+`, `-`, `~`
4. Multiplication, Division, Floor Division, Modulus `*`, `/`, `//`, `%`
5. Addition, Subtraction `+`, `-`
6. Bitwise shifts `<<`, `>>`
7. Bitwise AND `&`
8. Bitwise XOR `^`
9. Bitwise OR `|`
10. Comparisons `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `is not`, `in`, `not in`
11. Logical NOT `not`
12. Logical AND `and`
13. Logical OR `or`

## Best Practices

1. Use descriptive variable names
2. Follow PEP 8 naming conventions
3. Use parentheses to clarify operator precedence
4. Prefer `is` for `None` checks: `if x is None:`
5. Use `==` for value comparison, `is` for identity comparison
6. Be aware of short-circuit evaluation in logical operators

