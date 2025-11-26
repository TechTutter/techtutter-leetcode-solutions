# techtutter-leetocode-solutions

# Key Takeaways

## General

### Pass By Ref and By Value

In JavaScript everything is passed by value — more precisely, by a copy of the value.

- For primitives, the value is the value → the function receives a copy of it, so changes are not visible outside.
- For objects and arrays, the "value" being copied is the reference. This means:
  - you can modify the object through that reference (e.g. a.push(...))
  - but you cannot change the caller's variable (e.g. a = somethingElse only changes the local copy of the reference)

```typescript
let num = 4;
let nums = [1, 2, 3];

function myFunc(num, nums) {
  num += 1; // Not preserved outside (primitives are copied)
  nums.push(4); // Preserved (same referenced object is modified)
  nums = []; // Not preserved outside (only the local reference changes)
}
```

### In-place

> An in-place operation on an object / array modifies the original item without changing its reference. Tied to [Pass By Ref and By Value](###Pass-By-Ref-and-By-Value).

**Practical rule:** -> You can't reassign the origian value (e.g `nums = somethingElse`) but you can perform any other operation (e.g. `nums.push(...)`)

### Bit Shift Operators (>> and <<)

Shift by N bits. More efficient on CPU level.
Also automatically truncate (no need to do floor). This is because of bit nature.
E.g.

```typescript
const x = 10; // 1010
console.log(x >> 1); // 0101 -> 5
console.log(x >> 2); // 0010 -> 2
console.log(x >> 3); // 0001 -> 1
console.log(x >> 4); // 0000 -> 0
```

- x >> 1 is equal to Math.floor(x/2)
- x << 1 is equal to x\*2

## Arrays And Strings - See [readme.md](./arrays-and-strings/readme.md)
