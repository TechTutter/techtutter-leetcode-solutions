function canJump(nums: number[]): boolean {
  const len = nums.length;
  if (len < 2) return true;

  let cumulativeJumpDistance = 0;

  for (let i = len - 1; i >= 0; i--) {
    const currJumpDistance = nums[i];
    const canReachTarget = currJumpDistance >= cumulativeJumpDistance;
    if (!currJumpDistance || !canReachTarget) {
      cumulativeJumpDistance++;
    } else {
      cumulativeJumpDistance = 1;
    }
  }
  return cumulativeJumpDistance === 1 && nums[0] > 0;
}

export { canJump };
