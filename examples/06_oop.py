"""
Object-Oriented Programming Examples
=====================================
This file demonstrates classes, objects, inheritance, and OOP concepts.
"""

# ============================================================================
# BASIC CLASS AND OBJECT
# ============================================================================

print("=" * 60)
print("BASIC CLASS AND OBJECT")
print("=" * 60)

class Dog:
    """A simple Dog class"""
    
    # Class variable
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Initialize a Dog instance"""
        # Instance variables
        self.name = name
        self.age = age
    
    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says Woof!"
    
    def get_info(self):
        """Get dog information"""
        return f"{self.name} is {self.age} years old"

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())
print(dog2.get_info())
print(f"Species: {Dog.species}")

# ============================================================================
# INSTANCE, CLASS, AND STATIC METHODS
# ============================================================================

print("\n" + "=" * 60)
print("INSTANCE, CLASS, AND STATIC METHODS")
print("=" * 60)

class Calculator:
    """Calculator with different method types"""
    
    # Class variable
    operation_count = 0
    
    def __init__(self, value=0):
        self.value = value
    
    # Instance method
    def add(self, num):
        """Add to value"""
        self.value += num
        Calculator.operation_count += 1
        return self.value
    
    # Class method
    @classmethod
    def get_operation_count(cls):
        """Get total operation count"""
        return cls.operation_count
    
    @classmethod
    def from_string(cls, value_str):
        """Alternative constructor"""
        return cls(int(value_str))
    
    # Static method
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        Calculator.operation_count += 1
        return a * b

calc1 = Calculator(10)
calc2 = Calculator(20)

print(f"Calc1 value: {calc1.value}")
print(f"Calc1 add 5: {calc1.add(5)}")
print(f"Calc2 add 10: {calc2.add(10)}")
print(f"Total operations: {Calculator.get_operation_count()}")
print(f"Multiply 3 * 4: {Calculator.multiply(3, 4)}")

calc3 = Calculator.from_string("100")
print(f"Created from string: {calc3.value}")

# ============================================================================
# SPECIAL METHODS (MAGIC/DUNDER METHODS)
# ============================================================================

print("\n" + "=" * 60)
print("SPECIAL METHODS")
print("=" * 60)

class Point:
    """Point class with special methods"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """User-friendly string representation"""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        """Developer-friendly string representation"""
        return f"Point(x={self.x}, y={self.y})"
    
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __lt__(self, other):
        """Less than comparison (by distance from origin)"""
        if isinstance(other, Point):
            dist_self = (self.x**2 + self.y**2)**0.5
            dist_other = (other.x**2 + other.y**2)**0.5
            return dist_self < dist_other
        return NotImplemented
    
    def __add__(self, other):
        """Addition operator"""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __len__(self):
        """Length (distance from origin)"""
        return int((self.x**2 + self.y**2)**0.5)

p1 = Point(3, 4)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(f"p1: {p1}")
print(f"repr(p1): {repr(p1)}")
print(f"p1 == p2: {p1 == p2}")
print(f"p1 == p3: {p1 == p3}")
print(f"p1 < p2: {p1 < p2}")
print(f"p1 + p2: {p1 + p2}")
print(f"len(p1): {len(p1)}")

# ============================================================================
# INHERITANCE
# ============================================================================

print("\n" + "=" * 60)
print("INHERITANCE")
print("=" * 60)

class Animal:
    """Base Animal class"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        """Make a sound"""
        return f"{self.name} makes a sound"
    
    def get_info(self):
        """Get animal information"""
        return f"{self.name} is {self.age} years old"

class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def speak(self):
        """Override speak method"""
        return f"{self.name} barks: Woof!"
    
    def fetch(self):
        """Dog-specific method"""
        return f"{self.name} fetches the ball"

class Cat(Animal):
    """Cat class inheriting from Animal"""
    
    def speak(self):
        """Override speak method"""
        return f"{self.name} meows: Meow!"

dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2)

print(dog.speak())
print(cat.speak())
print(dog.get_info())
print(dog.fetch())

# Multiple inheritance
class Flyable:
    """Mixin for flying capability"""
    
    def fly(self):
        return "Flying!"

class Swimmable:
    """Mixin for swimming capability"""
    
    def swim(self):
        return "Swimming!"

class Duck(Animal, Flyable, Swimmable):
    """Duck with multiple capabilities"""
    
    def speak(self):
        return f"{self.name} quacks: Quack!"

duck = Duck("Donald", 1)
print(f"\n{duck.speak()}")
print(duck.fly())
print(duck.swim())

# Method Resolution Order
print(f"\nDuck MRO: {Duck.__mro__}")

# ============================================================================
# ENCAPSULATION
# ============================================================================

print("\n" + "=" * 60)
print("ENCAPSULATION")
print("=" * 60)

class BankAccount:
    """Bank account with encapsulation"""
    
    def __init__(self, account_number, balance=0):
        # Public
        self.account_number = account_number
        # Protected (convention)
        self._balance = balance
        # Private
        self.__pin = "1234"
    
    def get_balance(self):
        """Get balance"""
        return self._balance
    
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount, pin):
        """Withdraw money"""
        if pin != self.__pin:
            return False
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

account = BankAccount("12345", 1000)
print(f"Account: {account.account_number}")
print(f"Balance: {account.get_balance()}")
account.deposit(500)
print(f"After deposit: {account.get_balance()}")
account.withdraw(200, "1234")
print(f"After withdrawal: {account.get_balance()}")

# Property decorators
class Temperature:
    """Temperature with property decorators"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit"""
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"\nTemperature: {temp.celsius}°C = {temp.fahrenheit}°F")
temp.celsius = 30
print(f"After setting: {temp.celsius}°C = {temp.fahrenheit}°F")
temp.fahrenheit = 86
print(f"After setting Fahrenheit: {temp.celsius}°C = {temp.fahrenheit}°F")

# ============================================================================
# POLYMORPHISM
# ============================================================================

print("\n" + "=" * 60)
print("POLYMORPHISM")
print("=" * 60)

# Duck typing
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm quacking like a duck!"

def make_quack(obj):
    """Function that works with any object that has quack()"""
    print(obj.quack())

duck = Duck()
person = Person()

make_quack(duck)
make_quack(person)

# Polymorphism with inheritance
shapes = [
    type('Circle', (), {'area': lambda self: 3.14 * 5**2})(),
    type('Rectangle', (), {'area': lambda self: 4 * 6})(),
    type('Square', (), {'area': lambda self: 3 * 3})()
]

for shape in shapes:
    print(f"Area: {shape.area()}")

# ============================================================================
# ABSTRACT CLASSES
# ============================================================================

print("\n" + "=" * 60)
print("ABSTRACT CLASSES")
print("=" * 60)

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented"""
        pass
    
    def describe(self):
        """Non-abstract method"""
        return f"Shape with area {self.area()} and perimeter {self.perimeter()}"

class Rectangle(Shape):
    """Rectangle implementation"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle implementation"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

rect = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle: {rect.describe()}")
print(f"Circle: {circle.describe()}")

# ============================================================================
# COMPOSITION
# ============================================================================

print("\n" + "=" * 60)
print("COMPOSITION")
print("=" * 60)

class Engine:
    """Engine class"""
    
    def start(self):
        return "Engine started"
    
    def stop(self):
        return "Engine stopped"

class Car:
    """Car class using composition"""
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine()  # Composition
    
    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"
    
    def stop(self):
        return f"{self.make} {self.model}: {self.engine.stop()}"

car = Car("Toyota", "Camry")
print(car.start())
print(car.stop())

