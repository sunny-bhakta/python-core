# Standard Library

## Overview
Python's standard library is extensive and provides modules for common tasks. This section covers essential standard library modules.

## Essential Modules

### os Module
Operating system interface.

**Common Functions:**
- `os.getcwd()` - Get current directory
- `os.chdir(path)` - Change directory
- `os.listdir(path)` - List directory contents
- `os.mkdir(path)` - Create directory
- `os.remove(path)` - Remove file
- `os.rename(old, new)` - Rename file
- `os.path.*` - Path operations

### sys Module
System-specific parameters and functions.

**Common Functions:**
- `sys.argv` - Command-line arguments
- `sys.exit()` - Exit program
- `sys.path` - Module search path
- `sys.version` - Python version
- `sys.platform` - Platform identifier
- `sys.stdin`, `sys.stdout`, `sys.stderr` - Standard streams

### math Module
Mathematical functions.

**Common Functions:**
- `math.pi`, `math.e` - Constants
- `math.sqrt(x)` - Square root
- `math.pow(x, y)` - Power
- `math.sin()`, `math.cos()`, `math.tan()` - Trigonometry
- `math.log()`, `math.exp()` - Logarithms
- `math.ceil()`, `math.floor()` - Rounding
- `math.factorial()` - Factorial

### random Module
Random number generation.

**Common Functions:**
- `random.random()` - Random float [0.0, 1.0)
- `random.randint(a, b)` - Random integer
- `random.choice(seq)` - Random choice
- `random.shuffle(seq)` - Shuffle sequence
- `random.sample(population, k)` - Random sample

### datetime Module
Date and time handling.

**Classes:**
- `datetime.datetime` - Date and time
- `datetime.date` - Date only
- `datetime.time` - Time only
- `datetime.timedelta` - Time difference

**Common Functions:**
- `datetime.now()` - Current date/time
- `datetime.strftime()` - Format string
- `datetime.strptime()` - Parse string

### json Module
JSON encoder and decoder.

**Functions:**
- `json.dumps(obj)` - Convert to JSON string
- `json.loads(s)` - Parse JSON string
- `json.dump(obj, file)` - Write to file
- `json.load(file)` - Read from file

### csv Module
CSV file reading and writing.

**Functions:**
- `csv.reader()` - Read CSV
- `csv.writer()` - Write CSV
- `csv.DictReader()` - Read as dictionary
- `csv.DictWriter()` - Write from dictionary

### re Module
Regular expressions.

**Functions:**
- `re.search()` - Find pattern
- `re.match()` - Match at start
- `re.findall()` - Find all matches
- `re.sub()` - Replace matches
- `re.compile()` - Compile pattern

### collections Module
Specialized container datatypes.

**Classes:**
- `Counter` - Count hashable objects
- `defaultdict` - Dictionary with default factory
- `OrderedDict` - Dictionary with order
- `deque` - Double-ended queue
- `namedtuple` - Tuple with named fields

### itertools Module
Iterator functions.

**Functions:**
- `itertools.count()` - Infinite counter
- `itertools.cycle()` - Cycle through iterable
- `itertools.repeat()` - Repeat value
- `itertools.chain()` - Chain iterables
- `itertools.combinations()` - Combinations
- `itertools.permutations()` - Permutations

### functools Module
Higher-order functions.

**Functions:**
- `functools.partial()` - Partial function
- `functools.reduce()` - Reduce function
- `functools.wraps()` - Preserve metadata
- `functools.lru_cache()` - Caching decorator

### operator Module
Standard operators as functions.

**Functions:**
- `operator.add()`, `operator.sub()` - Arithmetic
- `operator.mul()`, `operator.truediv()` - Arithmetic
- `operator.eq()`, `operator.lt()` - Comparisons
- `operator.itemgetter()` - Item getter
- `operator.attrgetter()` - Attribute getter

### urllib Module
URL handling.

**Submodules:**
- `urllib.request` - Open URLs
- `urllib.parse` - Parse URLs
- `urllib.error` - Exception classes

### http Module
HTTP modules.

**Submodules:**
- `http.client` - HTTP client
- `http.server` - HTTP server

### sqlite3 Module
SQLite database interface.

**Functions:**
- `sqlite3.connect()` - Connect to database
- `connection.execute()` - Execute SQL
- `connection.commit()` - Commit transaction
- `connection.close()` - Close connection

### logging Module
Logging facility.

**Functions:**
- `logging.basicConfig()` - Basic configuration
- `logging.debug()`, `logging.info()` - Log messages
- `logging.warning()`, `logging.error()` - Log messages
- `logging.critical()` - Log messages

**Levels:**
- DEBUG, INFO, WARNING, ERROR, CRITICAL

### unittest Module
Unit testing framework.

**Classes:**
- `unittest.TestCase` - Test case base class
- `unittest.TestSuite` - Test suite
- `unittest.TestLoader` - Test loader

**Methods:**
- `setUp()` - Setup before each test
- `tearDown()` - Cleanup after each test
- `assertEqual()`, `assertTrue()` - Assertions

### pdb Module
Python debugger.

**Functions:**
- `pdb.set_trace()` - Set breakpoint
- `pdb.post_mortem()` - Post-mortem debugging

### argparse Module
Command-line argument parsing.

**Classes:**
- `argparse.ArgumentParser` - Parser
- `parser.add_argument()` - Add argument
- `parser.parse_args()` - Parse arguments

### pathlib Module
Object-oriented filesystem paths.

**Classes:**
- `Path` - Path object
- Methods: `exists()`, `is_file()`, `is_dir()`
- Methods: `read_text()`, `write_text()`
- Methods: `mkdir()`, `rmdir()`

### typing Module
Type hints support.

**Types:**
- `typing.List`, `typing.Dict`, `typing.Tuple`
- `typing.Optional`, `typing.Union`
- `typing.Callable`, `typing.Iterable`

## Best Practices

1. Familiarize yourself with standard library
2. Use standard library before third-party packages
3. Read module documentation
4. Understand module purpose and use cases
5. Use appropriate module for task
6. Check module version compatibility
7. Import only what you need
8. Use `from module import` for clarity
9. Handle module-specific exceptions
10. Keep up with new modules in Python versions

