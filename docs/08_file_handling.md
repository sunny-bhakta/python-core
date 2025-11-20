# File Handling

## Overview
File handling allows programs to read from and write to files on the filesystem. Python provides built-in functions and modules for file operations.

## File Operations

### Opening Files

**`open()` function:**
```python
file = open(filename, mode)
```

**File Modes:**
- `'r'` - Read (default, text mode)
- `'w'` - Write (overwrites existing)
- `'a'` - Append (adds to end)
- `'x'` - Exclusive creation (fails if exists)
- `'b'` - Binary mode (e.g., `'rb'`, `'wb'`)
- `'t'` - Text mode (default)
- `'+'` - Read and write (e.g., `'r+'`, `'w+'`)

### Reading Files

**Methods:**
- `read()` - Read entire file
- `readline()` - Read single line
- `readlines()` - Read all lines into list
- Iteration - `for line in file:`

### Writing Files

**Methods:**
- `write(string)` - Write string
- `writelines(sequence)` - Write sequence of strings

### Closing Files

**Important:** Always close files to free resources.

**Methods:**
- `file.close()` - Explicit close
- `with` statement - Automatic close (recommended)

## Context Managers (with statement)

**Syntax:**
```python
with open(filename, mode) as file:
    # file operations
    pass
# File automatically closed
```

**Benefits:**
- Automatic file closing
- Exception handling
- Cleaner code

## File Paths

### os.path Module

**Common Functions:**
- `os.path.join(path1, path2)` - Join paths
- `os.path.exists(path)` - Check if path exists
- `os.path.isfile(path)` - Check if file
- `os.path.isdir(path)` - Check if directory
- `os.path.basename(path)` - Get filename
- `os.path.dirname(path)` - Get directory
- `os.path.split(path)` - Split path
- `os.path.splitext(path)` - Split extension

### pathlib Module (Python 3.4+)

**Path Objects:**
```python
from pathlib import Path

path = Path("file.txt")
path.exists()
path.read_text()
path.write_text("content")
```

**Benefits:**
- Object-oriented
- Cross-platform
- More intuitive

### Absolute vs Relative Paths

- **Absolute:** Full path from root (`/home/user/file.txt` or `C:\Users\file.txt`)
- **Relative:** Path relative to current directory (`./file.txt` or `../file.txt`)

## Common File Operations

### Reading Text Files

```python
with open('file.txt', 'r') as f:
    content = f.read()
```

### Writing Text Files

```python
with open('file.txt', 'w') as f:
    f.write("Hello, World!")
```

### Appending to Files

```python
with open('file.txt', 'a') as f:
    f.write("New line\n")
```

### Reading Line by Line

```python
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

### Binary Files

```python
with open('image.jpg', 'rb') as f:
    data = f.read()
```

## Best Practices

1. Always use `with` statement
2. Handle file exceptions (FileNotFoundError, PermissionError)
3. Use appropriate file modes
4. Close files explicitly if not using `with`
5. Use `pathlib` for path operations (Python 3.4+)
6. Handle encoding for text files (`encoding='utf-8'`)
7. Use binary mode for non-text files
8. Check file existence before operations
9. Use absolute paths when needed
10. Clean up temporary files

