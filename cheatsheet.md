# Functions

Use `def`. For generic arguments, use \*a syntax, for keyword arguments use \*\*b syntax (a and b can be renamed to whatever). Keyword arguments must be declared after generic arguments.

````python
def my_func(a, *args, **kwargs):
    print(a, b, c)

my_func(10, 20, 30, 40, 50, 60, x=1, y=2)

# Lists

```python
my_list = ["Apple", 1, True]
another_list = list(("apple", "banana", "cherry"))
print(len(my_list)) # 3

````
