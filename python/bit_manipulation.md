# Bit Manipulation

# Conversions

```python
to_binary = bin(n)[2:]
to_int = int(binary_string, 2)

```

# Bitwise Operators

## Shift
```python
"""
23 is 10111. 
A shift left is equiv to 101110. 
A shift right is equiv to 1011
"""
x = 23
x << 1 # 46 - equiv to x * 2
x >> 1 # 11 - equiv to math.floor(x / 2)
```
## XOR
```python
"""
XOR (a ^ b) return 0 if bits are the same, and is equivalent to sum bit without carry
"""
x = 0
a = 9
b = 1

a ^ a # 0
a ^ b # 10

```

```python
AND = n & 1
OR = n | 1
XOR = n ^ 1
NOT = ~n
Left Shift = n << 1
Right Shift = n >> 1
```