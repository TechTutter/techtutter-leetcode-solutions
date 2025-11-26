// Can k be greater then nums lenght ? Yes
// Rotations of 0 or nums.length * N are the same, no movement is required
// Rotations by anything else, pick a slice starting from len - 1 - k + 1 -> len - k
// Append remaining elements from start to len len - k - 1

/**
 Do not return anything, modify nums in-place instead.
 */

// A rotation, unlike swap, requires 2 tmp stored values, prev and curr
function rotate(nums: number[], k: number): void {
  const len = nums.length;
  const rotations = k % len;
  if (!rotations) return;
  if (nums.length < 2) return;

  let j: number | undefined;
  for (let i = 0; i < rotations; i++) {
    j = (i + 1) % len;
    const startIdx = j > 0 ? j - 1 : len - 1;
    let tmpA: number | undefined;
    let tmpB = nums[startIdx];
    let idx = i + 1;

    for (let j = 0; j < len; j++) {
      tmpA = nums[idx];
      nums[idx] = tmpB;
      tmpB = tmpA;
      idx = (idx + 1) % len;
    }
  }
}

function revert(nums: number[], start: number, end: number) {
  if (start === end || nums.length < 2) return;
  if (start > end) throw new Error("start must be lower than end");

  let i = start,
    j = end;
  let tmp = 0;
  while (i < j) {
    tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
    i++;
    j--;
  }
}

function rotate2(nums: number[], k: number): void {
  const len = nums.length;
  const rotations = k % len;
  if (!rotations) return;
  if (len < 2) return;

  revert(nums, 0, len - 1);
  revert(nums, 0, rotations - 1);
  revert(nums, rotations, len - 1);
}

export { rotate, rotate2 };
