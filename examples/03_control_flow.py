"""
Control Flow Examples
====================
This file demonstrates conditional statements, loops, and loop control in Python.
"""

# ============================================================================
# CONDITIONAL STATEMENTS
# ============================================================================

print("=" * 60)
print("CONDITIONAL STATEMENTS")
print("=" * 60)

# Simple if statement
age = 20
if age >= 18:
    print(f"Age {age}: You are an adult")

# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")

# if-elif-else statement
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score {score} = Grade {grade}")

# Multiple elif statements
day = "Wednesday"
if day == "Monday":
    print("Start of work week")
elif day == "Friday":
    print("TGIF!")
elif day in ["Saturday", "Sunday"]:
    print("Weekend!")
else:
    print("Midweek")

# Nested if statements
x, y = 10, 5
if x > 0:
    if y > 0:
        print("Both x and y are positive")
    else:
        print("x is positive, y is not")
else:
    print("x is not positive")

# Ternary operator (conditional expression)
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

# Ternary with multiple conditions
score = 85
result = "Excellent" if score >= 90 else "Good" if score >= 70 else "Needs improvement"
print(f"Score {score}: {result}")

# Chained comparisons
x = 5
if 1 < x < 10:
    print(f"{x} is between 1 and 10")

if 0 <= x <= 100:
    print(f"{x} is between 0 and 100 (inclusive)")

# Multiple conditions with logical operators
username = "admin"
password = "secret123"
if username == "admin" and password == "secret123":
    print("Access granted")
else:
    print("Access denied")

# ============================================================================
# FOR LOOPS
# ============================================================================

print("\n" + "=" * 60)
print("FOR LOOPS")
print("=" * 60)

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# Iterating over a string
word = "Python"
print(f"\nCharacters in '{word}':")
for char in word:
    print(f"  {char}")

# Using range()
print("\nNumbers 0 to 4:")
for i in range(5):
    print(f"  {i}")

print("\nNumbers 2 to 6:")
for i in range(2, 7):
    print(f"  {i}")

print("\nEven numbers 0 to 8:")
for i in range(0, 10, 2):
    print(f"  {i}")

print("\nCountdown from 5 to 1:")
for i in range(5, 0, -1):
    print(f"  {i}")

# enumerate() - getting index and value
print("\nUsing enumerate():")
items = ["first", "second", "third"]
for index, item in enumerate(items):
    print(f"  Index {index}: {item}")

# enumerate() with start parameter
print("\nEnumerate starting from 1:")
for index, item in enumerate(items, start=1):
    print(f"  Position {index}: {item}")

# zip() - iterating over multiple sequences
print("\nUsing zip():")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age} years old, from {city}")

# Nested for loops
print("\nNested loops (multiplication table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i * j}", end="  ")
    print()  # New line after each row

# Iterating over dictionary
person = {"name": "Alice", "age": 30, "city": "NYC"}
print("\nDictionary iteration:")
for key in person:
    print(f"  {key}: {person[key]}")

print("\nUsing .items():")
for key, value in person.items():
    print(f"  {key}: {value}")

# ============================================================================
# WHILE LOOPS
# ============================================================================

print("\n" + "=" * 60)
print("WHILE LOOPS")
print("=" * 60)

# Basic while loop
count = 0
print("Counting to 5:")
while count < 5:
    print(f"  Count: {count}")
    count += 1

# While loop with user input simulation
print("\nSimulated user input (countdown):")
counter = 5
while counter > 0:
    print(f"  {counter}...")
    counter -= 1
print("  Go!")

# While loop with condition
print("\nFinding first even number:")
numbers = [1, 3, 5, 8, 9, 10]
index = 0
while index < len(numbers) and numbers[index] % 2 != 0:
    index += 1
if index < len(numbers):
    print(f"  First even number: {numbers[index]} at index {index}")

# ============================================================================
# LOOP CONTROL: break
# ============================================================================

print("\n" + "=" * 60)
print("LOOP CONTROL: break")
print("=" * 60)

# break in for loop
print("Searching for 'banana' in list:")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "banana":
        print(f"  Found {fruit}!")
        break
    print(f"  Checking {fruit}...")

# break in while loop
print("\nCountdown with break:")
count = 10
while count > 0:
    print(f"  {count}")
    count -= 1
    if count == 5:
        print("  Breaking at 5!")
        break

# break in nested loops (only breaks inner loop)
print("\nNested loops with break:")
for i in range(3):
    print(f"  Outer loop: {i}")
    for j in range(5):
        if j == 2:
            print(f"    Breaking inner loop at j={j}")
            break
        print(f"    Inner loop: {j}")

# ============================================================================
# LOOP CONTROL: continue
# ============================================================================

print("\n" + "=" * 60)
print("LOOP CONTROL: continue")
print("=" * 60)

# continue in for loop - skip even numbers
print("Printing only odd numbers:")
for num in range(10):
    if num % 2 == 0:
        continue
    print(f"  {num}")

# continue - skip specific items
print("\nSkipping 'banana':")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(f"  {fruit}")

# continue in while loop
print("\nWhile loop with continue:")
count = 0
while count < 10:
    count += 1
    if count % 3 == 0:
        continue
    print(f"  {count}")

# ============================================================================
# LOOP CONTROL: pass
# ============================================================================

print("\n" + "=" * 60)
print("LOOP CONTROL: pass")
print("=" * 60)

# pass as placeholder
for i in range(5):
    if i % 2 == 0:
        pass  # Do nothing for even numbers
    else:
        print(f"  Odd number: {i}")

# pass in empty function (will be covered in functions section)
def placeholder_function():
    pass  # To be implemented later

# ============================================================================
# else CLAUSE IN LOOPS
# ============================================================================

print("\n" + "=" * 60)
print("else CLAUSE IN LOOPS")
print("=" * 60)

# else in for loop - executes if no break
print("Searching for item (not found case):")
items = [1, 2, 3, 4, 5]
for item in items:
    if item == 10:
        print(f"  Found {item}!")
        break
else:
    print("  Item not found in list")

# else in for loop - executes if break occurs
print("\nSearching for item (found case):")
for item in items:
    if item == 3:
        print(f"  Found {item}!")
        break
else:
    print("  Item not found in list")

# else in while loop
print("\nWhile loop with else:")
count = 0
while count < 3:
    print(f"  Count: {count}")
    count += 1
else:
    print("  Loop completed normally")

# else with break
print("\nWhile loop with break (else not executed):")
count = 0
while count < 5:
    if count == 2:
        print(f"  Breaking at {count}")
        break
    print(f"  Count: {count}")
    count += 1
else:
    print("  This won't print")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Finding maximum in list
numbers = [3, 7, 2, 9, 1, 5]
max_num = numbers[0]
for num in numbers[1:]:
    if num > max_num:
        max_num = num
print(f"Maximum in {numbers}: {max_num}")

# Example 2: Sum of numbers
total = 0
for num in range(1, 11):
    total += num
print(f"Sum of 1 to 10: {total}")

# Example 3: Factorial
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n}: {factorial}")

# Example 4: Prime number check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("\nPrime numbers from 1 to 20:")
for num in range(1, 21):
    if is_prime(num):
        print(f"  {num} is prime")

# Example 5: Pattern printing
print("\nPattern (right triangle):")
for i in range(1, 6):
    print("  " + "*" * i)

# Example 6: List comprehension alternative (preview)
print("\nSquares of numbers 1-5:")
squares = [x**2 for x in range(1, 6)]
print(f"  {squares}")

