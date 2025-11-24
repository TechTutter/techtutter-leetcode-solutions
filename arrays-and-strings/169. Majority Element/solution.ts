// Smart Solution for linear time and O(1) space
function majorityElement(nums: number[]): number {
  let candidate: number = 0;
  let occurrencies: number = 0;

  for (let num of nums) {
    if (occurrencies === 0) candidate = num;
    occurrencies += num === candidate ? 1 : -1;
  }
  return candidate;
}

// Simpler solution, Sort (O(n log(n)) and just pick the middle (O(1))
// Shift >> 1 is equal to Math.floor(nums.length/2), divide by 2 and truncate
function majorityElement2(nums: number[]): number {
  if (nums.length === 1) return nums[0];
  nums = quicksort(nums);
  return nums[nums.length >> 1];
}

function quicksort(arr: number[]): number[] {
  if (arr.length < 2) return arr;
  const pivot = arr[arr.length >> 1];
  const left: number[] = [];
  const right: number[] = [];
  const equal: number[] = [];

  for (const x of arr) {
    if (x < pivot) left.push(x);
    else if (x > pivot) right.push(x);
    else equal.push(x);
  }

  return [...quicksort(left), ...equal, ...quicksort(right)];
}

export { majorityElement, majorityElement2 };
