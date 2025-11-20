"""
File Handling Examples
======================
This file demonstrates file operations, reading, writing, and path handling.
"""

import os
from pathlib import Path

# ============================================================================
# BASIC FILE OPERATIONS
# ============================================================================

print("=" * 60)
print("BASIC FILE OPERATIONS")
print("=" * 60)

# Writing to a file
filename = "example.txt"
with open(filename, 'w') as f:
    f.write("Hello, World!\n")
    f.write("This is line 2\n")
    f.write("This is line 3\n")

print(f"Created file: {filename}")

# Reading entire file
with open(filename, 'r') as f:
    content = f.read()
    print(f"\nFile content (read()):\n{content}")

# Reading line by line
print("File content (line by line):")
with open(filename, 'r') as f:
    for line_num, line in enumerate(f, 1):
        print(f"  Line {line_num}: {line.strip()}")

# Reading all lines into list
with open(filename, 'r') as f:
    lines = f.readlines()
    print(f"\nAll lines (readlines()): {lines}")

# Reading single line
with open(filename, 'r') as f:
    first_line = f.readline()
    print(f"First line (readline()): {first_line.strip()}")

# ============================================================================
# FILE MODES
# ============================================================================

print("\n" + "=" * 60)
print("FILE MODES")
print("=" * 60)

# Write mode (overwrites)
with open("write_mode.txt", 'w') as f:
    f.write("This overwrites existing content\n")

# Append mode
with open("append_mode.txt", 'a') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

with open("append_mode.txt", 'a') as f:
    f.write("Line 3 (appended)\n")

print("Append mode - added to existing file")
with open("append_mode.txt", 'r') as f:
    print(f.read())

# Read and write mode
with open("readwrite.txt", 'w+') as f:
    f.write("Initial content\n")
    f.seek(0)  # Go back to beginning
    content = f.read()
    print(f"Read-write mode: {content}")

# ============================================================================
# CONTEXT MANAGERS (with statement)
# ============================================================================

print("\n" + "=" * 60)
print("CONTEXT MANAGERS")
print("=" * 60)

# Automatic file closing
def demonstrate_context_manager():
    with open("context_demo.txt", 'w') as f:
        f.write("File opened with context manager\n")
        print("  File is open inside 'with' block")
    print("  File is automatically closed outside 'with' block")

demonstrate_context_manager()

# Multiple files
with open("file1.txt", 'w') as f1, open("file2.txt", 'w') as f2:
    f1.write("Content in file 1\n")
    f2.write("Content in file 2\n")
print("Opened and closed multiple files simultaneously")

# ============================================================================
# FILE PATHS - os.path
# ============================================================================

print("\n" + "=" * 60)
print("FILE PATHS - os.path")
print("=" * 60)

# Current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Join paths
file_path = os.path.join(current_dir, "example.txt")
print(f"Joined path: {file_path}")

# Check if file exists
print(f"File exists: {os.path.exists('example.txt')}")
print(f"Is file: {os.path.isfile('example.txt')}")
print(f"Is directory: {os.path.isdir('example.txt')}")

# Path components
print(f"\nPath components:")
print(f"  Basename: {os.path.basename(file_path)}")
print(f"  Dirname: {os.path.dirname(file_path)}")
print(f"  Split: {os.path.split(file_path)}")
print(f"  Splitext: {os.path.splitext('example.txt')}")

# ============================================================================
# FILE PATHS - pathlib
# ============================================================================

print("\n" + "=" * 60)
print("FILE PATHS - pathlib")
print("=" * 60)

# Creating Path objects
path = Path("example.txt")
print(f"Path object: {path}")
print(f"Exists: {path.exists()}")
print(f"Is file: {path.is_file()}")
print(f"Parent: {path.parent}")
print(f"Name: {path.name}")
print(f"Suffix: {path.suffix}")
print(f"Stem: {path.stem}")

# Reading and writing with pathlib
pathlib_file = Path("pathlib_demo.txt")
pathlib_file.write_text("Content written with pathlib\n")
content = pathlib_file.read_text()
print(f"\nContent from pathlib: {content}")

# Path operations
new_path = Path("subdir") / "file.txt"
print(f"Joined path: {new_path}")

# ============================================================================
# BINARY FILES
# ============================================================================

print("\n" + "=" * 60)
print("BINARY FILES")
print("=" * 60)

# Writing binary data
binary_data = b"Binary content\nMore binary data"
with open("binary_file.bin", 'wb') as f:
    f.write(binary_data)

# Reading binary data
with open("binary_file.bin", 'rb') as f:
    read_data = f.read()
    print(f"Binary data read: {read_data}")

# ============================================================================
# ERROR HANDLING
# ============================================================================

print("\n" + "=" * 60)
print("ERROR HANDLING")
print("=" * 60)

# FileNotFoundError
try:
    with open("nonexistent.txt", 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("  File not found - handled gracefully")

# PermissionError (if applicable)
try:
    with open("/root/protected.txt", 'w') as f:
        f.write("test")
except PermissionError:
    print("  Permission denied - handled gracefully")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Reading CSV-like data
csv_data = "Name,Age,City\nAlice,30,NYC\nBob,25,LA\nCharlie,35,Chicago"
with open("data.csv", 'w') as f:
    f.write(csv_data)

print("CSV file created")
with open("data.csv", 'r') as f:
    for line in f:
        print(f"  {line.strip()}")

# Example 2: Logging to file
with open("app.log", 'a') as f:
    f.write("2024-01-01 10:00:00 - Application started\n")
    f.write("2024-01-01 10:01:00 - User logged in\n")
    f.write("2024-01-01 10:02:00 - Data processed\n")

print("\nLog file entries:")
with open("app.log", 'r') as f:
    for line in f:
        print(f"  {line.strip()}")

# Example 3: File copy
with open("source.txt", 'w') as f:
    f.write("Source file content\n")

with open("source.txt", 'r') as src, open("destination.txt", 'w') as dst:
    dst.write(src.read())

print("\nFile copied:")
with open("destination.txt", 'r') as f:
    print(f"  {f.read().strip()}")

# Example 4: Reading configuration
config_content = "host=localhost\nport=8080\ndebug=True"
with open("config.txt", 'w') as f:
    f.write(config_content)

config = {}
with open("config.txt", 'r') as f:
    for line in f:
        if '=' in line:
            key, value = line.strip().split('=', 1)
            config[key] = value

print(f"\nConfiguration loaded: {config}")

# Cleanup
files_to_remove = [
    "example.txt", "write_mode.txt", "append_mode.txt", "readwrite.txt",
    "context_demo.txt", "file1.txt", "file2.txt", "pathlib_demo.txt",
    "binary_file.bin", "data.csv", "app.log", "source.txt", "destination.txt",
    "config.txt"
]

print("\nCleaning up temporary files...")
for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
        print(f"  Removed: {file}")

