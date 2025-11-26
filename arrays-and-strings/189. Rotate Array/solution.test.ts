import { describe, it, expect } from "vitest";
import { rotate, rotate2 } from "./solution";
describe("Rotate Array", () => {
  it("testcase1", () => {
    const nums1 = [1, 2, 3, 4, 5, 6, 7];
    const nums2 = [1, 2, 3, 4, 5, 6, 7];
    const k = 3;
    const expected = [5, 6, 7, 1, 2, 3, 4];

    rotate(nums1, k);
    rotate2(nums2, k);
    expect(nums1).toEqual(expected);
    expect(nums2).toEqual(expected);
  });

  it("testcase2", () => {
    const nums1 = [-1, -100, 3, 99];
    const nums2 = [-1, -100, 3, 99];
    const k = 2;
    const expected = [3, 99, -1, -100];

    rotate(nums1, k);
    rotate2(nums2, k);
    expect(nums1).toEqual(expected);
    expect(nums2).toEqual(expected);
  });
});
