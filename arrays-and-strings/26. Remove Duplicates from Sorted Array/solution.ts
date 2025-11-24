// We can't use any helper data structure, we need to perform it in plaace so we proceed with two pointers and a series of swaps
// O(n)
function removeDuplicates(nums: number[]) {
  const totalNums = nums.length;
  if (totalNums < 2) return totalNums;

  let j = 1;
  let target = nums[0];
  let uniqueElementsCount = 1;

  for (let i = 1; i < totalNums; i++) {
    while (nums[j] === target && j < totalNums) {
      j++;
    }
    if (nums[j] > target) {
      target = nums[j];
      nums[i] = target;
      uniqueElementsCount++;
    }
  }
  nums.length = uniqueElementsCount;
  return uniqueElementsCount;
}

// Not valid solution !! It's not in-place, it creates a new array
function removeDuplicates2(nums: number[]) {
  const set = new Set(nums);
  nums.length = 0;
  nums.push(...Array.from(set));
  return set.size;
}

export { removeDuplicates };
