# techtutter-leetocode-solutions

# Key Takeaways

## General

### In-place

It means the algorithm modifies the input data without requiring extra space.

### Bit Shift Operators (>> and <<)

Shift by N bits. More efficient on CPU level.
Also automatically truncate (no need to do floor). This is because of bit nature.
E.g.

```typescript
x = 10; // 1010
console.log(x >> 1); // 0101 -> 5
console.log(x >> 2); // 0010 -> 2
console.log(x >> 3); // 0001 -> 1
console.log(x >> 4); // 0000 -> 0
```

- x >> 1 is equal to Math.floor(x/2)
- x << 1 is equal to x\*2

## Arrays And Strings - See [readme.md](./arrays-and-strings/readme.md)
