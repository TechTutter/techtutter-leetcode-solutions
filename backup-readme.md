# techtutter-leetocode-solutions

# Key Takeaways

## General

### Pass By Reference and By Value

In Python, everything is passed by object reference.

- For **immutable types** (int, float, str, tuple): the function receives a reference, but since they're immutable, you can't modify them. Reassignment creates a new object locally.
- For **mutable types** (list, dict, set): the function receives a reference to the same object, so modifications are visible outside.

```python
num = 4
nums = [1, 2, 3]

def my_func(num, nums):
    num += 1  # Not preserved outside (int is immutable, creates new local object)
    nums.append(4)  # Preserved (same referenced list is modified)
    nums = []  # Not preserved outside (only the local reference changes)
```

### In-place

> An in-place operation on a list modifies the original item without changing its reference. Tied to [Pass By Reference and By Value](#pass-by-reference-and-by-value).

**Practical rule:** -> You can't reassign the original value (e.g `nums = something_else`) but you can perform any other operation (e.g. `nums.append(...)`, `nums[:] = ...`)

### Bit Shift Operators (>> and <<)

Shift by N bits. More efficient on CPU level.
Also automatically truncate (no need to do floor). This is because of bit nature.

```python
x = 10  # 1010
print(x >> 1)  # 0101 -> 5
print(x >> 2)  # 0010 -> 2
print(x >> 3)  # 0001 -> 1
print(x >> 4)  # 0000 -> 0
```

- `x >> 1` is equal to `x // 2` (integer division)
- `x << 1` is equal to `x * 2`

## Arrays And Strings - See [readme.md](./arrays-and-strings/readme.md)
