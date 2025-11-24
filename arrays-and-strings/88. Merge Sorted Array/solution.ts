/**
  Readable solution
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  // get a slice of m - n elements as a reference, initialize i = 0, j = 0
  const nums1Copy = nums1.slice(0, m);
  let i = 0,
    j = 0,
    idx = 0;
  // main loop ->
  while (i < nums1Copy.length && j < nums2.length) {
    // compare i-th and j-th elements, add to i+j the lowest num
    nums1Copy[i] < nums2[j] ? (nums1[idx] = nums1Copy[i++]) : (nums1[idx] = nums2[j++]);
    idx = i + j;
  }

  // splice the rest
  if (i >= nums1Copy.length) nums1.splice(idx, nums1.length - idx, ...nums2.slice(j));
  else nums1.splice(idx, nums1.length - idx, ...nums1Copy.slice(i));
}

/**
 * Optimized solution
 */
function merge2(nums1: number[], m: number, nums2: number[], n: number): void {
  let i = m - 1;
  let j = n - 1;
  let k = m + n - 1;

  while (j >= 0) {
    if (i >= 0 && nums1[i] > nums2[j]) {
      nums1[k--] = nums1[i--];
    } else {
      nums1[k--] = nums2[j--];
    }
  }
}

export { merge };
