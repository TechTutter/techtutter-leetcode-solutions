# Python Core

## Variables and Print

```python
"""
Multiple values can be assigned to variables with comma separated values or "unpacking".
Variables can be reassigned to different types.
"""
text = "Hello, World!"
x, y = 1, 2
a, b = [1, 2] # Unpacking

a = "Orange" # Reassign to different type is allowed
```

```python
"""
Print allows for multiple comma separated values and formatted strings.
You can specify end character different from the default '\n'.
"""
print("Values of a and b are: ", a, b, end=", ")
print(f"Values of x is {x} and y is {y}")
```

```python
"""
All variables are global by default. Inside functions and classes, variables are local by default. `global` keyword is used to change this behavior.
"""
x = 5
y = 10
def func():
    x = 15 # local variable
    global y # global variable
    print(x, y) # 15 10 

    global z # since it doesn't exist, it creates a global variable
    z = 25
```

## Data Types and Type Hints
```python
""" Type hints are optional and do not enforce type checking, but make code more readable and self-documenting. Here are all the built-in data types.
"""
n: None = None

b: bool = True
i: int = 9
f: float = 5.2
z: complex = 2 + 3j

# Functions have type hints for parameters and return values 
def add(x: int, y: int) -> int:
    return x + y

# Custom classes can be used as type hints.
class Point:
    x: int
    y: int

p: Point = Point(1, 2)
```

```python
"""
Collections can be created using built-in functions, or alternatively using the short form with parentheses (with exception of sets)
"""
s: str = ""
l: list = []
d: dict = {}
t: tuple = ()
s: set = set()
fs: frozenset = frozenset() # immutable set

my_str: str = "Orange"
my_list: list[int] = [1, 2, 3]
my_dict: dict[str, int] = {"x": 1, "y": 2, "z": 3}
my_set: set[int] = {1, 2, 3}
my_tuple: tuple[int, int] = (1, 2)
```

```python
"""
Casting is done using built-in functions.
"""
char_x: str = str(x)
print(type(char_x)) # <class 'str'>
isinstance(char_x, str) # True
```

### Numbers
```python
"""
Some useful methods for numbers are listed here.
The full list of math ops can be seen at https://www.w3schools.com/python/module_math.asp
"""
max(5, 10) # output: 10
min(5, 10) # output: 5
abs(-5)    # output: 5

from math import pi, sqrt   
print(pi)               # output: 3.141592653589793
print(sqrt(4))          # output: 2.0
print(math.floor(5.2))  # output: 5
print(math.ceil(5.2))   # output: 6
print(math.trunc(5.2))  # output: 5

import random
print(random.random())      # output: random float between 0 and 1
print(random.randint(3, 9)) # output: random int between 3 and 9
```

### Strings
```python
"""
Strings are indexable and immutable collections of unicode characters. Char data type does not exist in python.
"""
text = "Hello, World!"
print(type(text)) # output: <class 'str'>
print(len(text))  # output: 41

multi_line_str = """This is a multi-line string.
Line breaks are preserved."""

CORE_FAMILY_MEMBERS = 7
formatted_str = f"Tutter family has {CORE_FAMILY_MEMBERS * 4} members"

print("Use + to combine with" + " " + text)
print("Use \n to add new line")
print("Use backslash to escape characters like \", \\, or \'")

x = text[0]    # output: "H"
y = text[-1]   # output: "d"
z = text[1:5]  # output: "ello"

for c in text:
    print(c)
```

```python
"""
Most useful string methods are listed here. For full list see https://www.w3schools.com/python/python_strings_methods.asp.

ALL string methods return new strings. They do not modify the original string.
"""
text: str = "Apple"

# Casing
text.upper()        # output: "APPLE"
text.lower()        # output: "apple"

# Searching
text.find("p")        # output: Index of first occurrence, -1 if not found.
text.find("p", 2, 5)  # Can also specify start | end ranges optionally.
text.startswith("Ap") # output: True
text.endswith("le")   # output: True

# Cleaning
text.strip()          # Clean whitespaces around. For left/right only, use lstrip() or rstrip()
text.replace("p", "") # Replace all occurrences
text.replace("p", "", 2) # Replace only first 2 occurrences

# Splitting and Joining
text.split("p")       # split on separator and return list of substrings
text.splitlines()     # Split at new line and return list of lines e.g. for file reading
"-".join(text)        # output: "A-p-p-l-e"
```

```python
"""
Regular expressions are used for pattern matching and text processing.
"""
import re

text = 'AY12345BZ'
match = re.search(r"\d+", "A123")          # output: Match object, e.g. if match
subbed = re.sub("\d", "X", "AY12345BZ")    # output: "AYXXXXXBZ"
splitted = re.split("\d+", "AB12CD34EF")   # output: ["AB", "CD", "EF"]
found = re.findall("\d+", "12A34")         # output: ["12", "34"]
```

### Lists

```python
"""
Lists are indexable, mutable collections, and allow duplicate values.
"""
l: list = [1, 2, True, 4, "Orange"]
print(type(l)) # output: <class 'list'>
print(len(l))  # output: 5
```

```python
"""
List Comprehensions are a concise way to create lists.
The format is [expr for item in iterable if condition].
"""
squares = [x * x for x in range(10)]
even_squares = [x * x for x in range(10) if x % 2 == 0]
combinations = [(x, y) for x in range(3) for y in range(3)]
```

```python
"""
Most useful list methods are listed here. For full list see https://www.w3schools.com/python/python_lists_methods.asp

ALL list methods are in-place. They do not return new lists.
"""
x: list = [1, 2, 3]

# Insertion
x.append(1)         # add element at end
x.insert(0, 15)     # add element at index 0
x.extend([1, 2, 3]) # add elements from any iterable, e.g. also x.extend((1, 2, 3))

# Removal
x.clear()           # remove all elements
x.remove(1)         # remove first occurrence of element
x.pop()             # remove and return last element
x.pop(3)            # remove and return element at index 3
del x[2]            # remove element at index 2

# Sorting
x.sort()            # as all operations, it is in-place
x.sort(reverse=True)
x.sort(key=len)     # sort with custom function
cars.sort(key=lambda e: (e.year, e.name)) # lambda is anonymous inline function

# Utility
x.copy()            # return shallow copy of list
x.reverse()         # reverse list in place
x.index(1)          # return index of first occurrence
```

### Tuple
```python
"""
Tuples are indexable, immutable collections, and allow duplicate values. Useful to return multiple values. Tuples only have a count and index methods.
"""
t: tuple = (1, 2, 3)
print(type(t)) # output: <class 'tuple'>
print(len(t))  # output: 3
print(t[1:3])  # output: (2, 3)

t.count(1) # output: number of occurrences
t.index(1) # output: index of first occurrence
```

```python
"""
Even though immutable, you can add two tuples using + operator.
"""
t1: tuple = (1, 2, 3)
t2: tuple = (4,)      # Tuple with 1 val needs a comma at the end or won't be recognized 
t1 += t2              # (1, 2, 3, 4)

del t2
```

### Set
```python
"""
Sets are unordered, mutable collections and do not allow duplicate values.
"""
s: set = {1, 2, 3}
print(type(s)) # output: <class 'set'>
print(len(s))  # output: 3
print(s[1:3])  # output: (2, 3)
```

```python
"""
Most useful set methods are listed here. For full list see https://www.w3schools.com/python/python_sets_methods.asp
"""
set_1: set = {1, 2, 3}
set_2 = {3, 4, 5}

# Insertion
set_1.add(1)          # does not add if already exists
set_1.update([1, 2, 3]) # add elements from any iterable, e.g. also x.update((1, 2, 3))

# Removal
set_1.clear()         # remove all elements
set_1.discard(5)      # remove first occurrence of element. Does not throw error if not found.

# Joining
set_3 = set_1.union(set_2)         # output: union of x and y
set_3 = set_1.intersection(set_2)  # output: only common elements
set_3 = set_1.difference(set_2)    # output: difference of x and y
set_3 = set_1.symmetric_difference(set_2) # output: only keep elements that are in one of the sets, but not both

"""
Most methods can be abbreviated with operators such as |, & etc.
Again, see 
"""
set_3 = set_1 | set_2 # union
set_3 = set_1 & set_2 # intersection
set_3 = set_1 - set_2 # difference
set_3 = set_1 ^ set_2 # symmetric difference
```

### Dictionary
```python
"""
Dictionaries are key-value pairs, and are mutable.
Use .get() to safely retrieve values.
"""
d: dict = {"x": 1, "y": 2}
print(type(d)) # output: <class 'dict'>
print(len(d))  # output: 2

# Insertion
d["z"] = 5
d.update({"x": 1, "n": 100, "h": 200})

# Retrieval and Iteration
val = d["x"]        # throws KeyError if key not found
val = d.get("y")    # returns None if key not found

for k, v in d.items():
    print(k, v)

for k in d.keys():
    print(d[k])

# Removal
d.clear()         # remove all elements
d.pop("x")        # remove element with key "x" and return value
del d["x"]        # remove element with key "x"
```

## Language Core

### Control Flow
```python
"""
Use indentation for elements in the same block.
- if, elif, else, match for condition blocks
- for, while for iteration blocks
- break, continue, pass for control flow
- and, or, not for boolean logic
"""
for i in range(10):
    if i % 2 == 0 and not i == 0 or i == 999:
        continue
    elif i == 5:
        break
    else:
        print(i)

while some_condition_holds:
    print("Error, Infinite Loop")

match condition:
    case 1 | 2 | 3:
        do_something()
    case 4 if some_condition:
        do_something()
    case 4:
        do_something_else()
    case _:
        do_default()

# Ternary Operator to execute or return values based on condition
print("A") if a > b else print("B")
print(1 if a > b else 2 if a < b else 0)
x = 1 if a > b else 2
```

### Functions
```python
"""
Functions are defined using def keyword. Params can have default values.
For generic arguments, use *args syntax, for keyword arguments use **kwargs syntax (args and kwargs can be renamed to whatever). Keyword arguments must be declared after generic arguments.
"""

# Can return multiple values. They will be packed into a tuple and can be unpacked.
def greet(name: str = "Tutter") -> str:
    return f"Hello {name}", "Some Other String"
str_1, str_2 = greet()

def sum_all_args_and_kwargs(a: int, *args: int | str, **kwargs: int | str) -> int:
    print(a)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

    all_args = [a] + list(args) + list(kwargs.values())
    parsed = [int(arg) for arg in all_args]
    return sum(parsed)

print(sum_all_args_and_kwargs(10, "20", "30", 40, 50, 60, x=1, y=2)) # 213

"""
Can also unpack lists and other iterables into function arguments using * operator.
Same for dictionaries with ** operator for kwargs.
"""
my_args = [1, 2, 3]
my_kwargs = {"x": 1, "y": 2}
sum_all_args_and_kwargs(10, *my_args, **my_kwargs)
# equivalent to
sum_all_args_and_kwargs(10, 1, 2, 3, x=1, y=2)
```

```python
"""
Lambda functions are anonymous inline functions. lambda <args> : <return value>
Often used with map(), filter(), sorted()
"""
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
evens = filter(lambda x: x % 2 == 0, numbers)
sorted_reversed = sorted(numbers, key=lambda x: x * -1)
```

```python
"""
Decorators take a function as argument and return a function.
Can use multiple at once, from inner to outer.
Optionally to preserve metadata use functools.wraps.
"""
import functools
def titlecase(func):
  @functools.wraps(func) # Optional, Preserves the metadata of the original function
  def myinner():
    return func().title()
  return myinner

def add_greeting(func):
  @functools.wraps(func)
  def myinner():
    return "hello " + func()
  return myinner

@titlecase
@add_greeting
def myfunction():
  return "have a great day!"
```

```python
"""
Generators are functions. They return an iterable generator object.
You can generate then next yeld value with next() or for loop.
They do not take up memory for the entire sequence, but generate values on the fly.
"""
def generator_function():
    yield 1
    yield 2
    yield 3

my_gen = generator_function()
print(next(my_gen)) # output: 1
print(next(my_gen)) # output: 2
print(next(my_gen)) # output: 3

my_seq = generator_function()
for i in my_seq:
    print(i)
```

## Exceptions
```python
"""
Try-except blocks are used to handle exceptions.
"""
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No error occurred")
finally:
    print("This will always run")

## Raise My Own Exception
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise MyException("This is my exception")
except MyException as e:
    print(e)
```

# Skipped Topics to Check later
- Iterators ( add it to the classes section ) __iter__ and __next__ etc.
- JSON ( add it to FILES section )
- For strings, lists etc add that you can use len, typeof, isinstance, slicing, "in" operator, UNPACKING, STAR * OPERATOR (super cool btw), COMPREHENSIONS, loops, product with * of iterable, can work for most of the collections
