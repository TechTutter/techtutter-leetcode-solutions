# Strings

```python
"""
Strings are indexable and immutable collections of unicode characters. Char data type does not exist in python.
"""
text: str = "Apple"

text[::-1]     # reverse string
text[:3]       # prefix
text[3:]       # suffix

# Casing
text.upper()        # output: "APPLE"
text.lower()        # output: "apple"

# Matching
text.isalpha()      # output: True if all characters are alphabetic
text.isdigit()      # output: True if all characters are digits
text.isalnum()      # output: True if all characters are alphanumeric

# Searching
text.find("p")        # output: Index of first occurrence, -1 if not found.
text.find("p", 2, 5)  # Can also specify start | end ranges optionally.
text.startswith("Ap") # output: True
text.endswith("le")   # output: True

# Cleaning
text.strip().trim().  # Cleanup whitespace
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

# Useful patterns

```python
# String builder
chars = []
chars.append("a")
chars.append("b")
result = "".join(chars)

# Anagram signature
''.join(sorted(text))

# Map char to "index"
idx = ord(c) - ord('a')

# Frequency count
from collections import Counter
count = Counter(text) # -> {"a": 1, "b": 15, ...}