function removeDuplicates(nums: number[]): number {
  let j = 2;
  const numsLength = nums.length;
  if (numsLength < 2) return numsLength;

  for (let i = 2; i < nums.length; i++) {
    if (nums[i] > nums[j - 2]) {
      nums[j] = nums[i];
      j++;
    }
  }

  return j;
}

export { removeDuplicates };
