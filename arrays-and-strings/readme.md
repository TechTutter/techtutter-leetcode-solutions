# Arrays And Strings

### Easily Truncate an Array in O(1)

To remove elements from the array, you can set the length to a lower value and truncate it to dereference them.

```typescript
const x = [0, 1, 2, 3, 4, 5];
x.length = 2;
console.log(x); // -> [0,1]
```

### Rotate array k times

Double rotation. Full rotation + 2 partial rotations, see [189. Rotate Array](189.%20Rotate%20Array/solution.ts)
Useful e.g. for truncating values in-place at the start, while preserving relative order.

### Useful Built-in Methods for arrays

```typescript
// Todo add this section from https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
const x = [1, 2, 3, 4, 5];
```
