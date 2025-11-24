function removeElement(nums: number[], val: number): number {
  if (!nums.length) return 0;

  let count = 0,
    i = 0,
    j = nums.length - 1;
  while (i != j) {
    if (nums[i] === val) {
      nums[i] = nums[j--];
      count++;
    } else i++;
  }

  if (nums[i] === val) count++;
  nums.splice(nums.length - count);

  return nums.length;
}

export { removeElement };
