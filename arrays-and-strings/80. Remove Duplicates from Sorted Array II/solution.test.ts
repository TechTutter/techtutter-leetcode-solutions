import { describe, it, expect } from "vitest";
import { removeDuplicates } from "./solution";

describe("Remove Duplicates from Sorted Array II", () => {
  it("testcase1", () => {
    const nums = [1, 1, 1, 1, 1, 2, 2, 2, 3];
    const expected = 5;
    const result = removeDuplicates(nums);
    nums.length = result;
    expect(result).toEqual(expected);
    expect(nums).toEqual([1, 1, 2, 2, 3]);
  });

  it("testcase2", () => {
    const nums = [0, 0, 1, 1, 1, 1, 2, 3, 3];
    const expected = 7;
    const result = removeDuplicates(nums);
    nums.length = result;
    expect(result).toEqual(expected);
    expect(nums).toEqual([0, 0, 1, 1, 2, 3, 3]);
  });
});
