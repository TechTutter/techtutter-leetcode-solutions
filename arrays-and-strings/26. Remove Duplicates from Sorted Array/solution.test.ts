import { describe, it, expect } from "vitest";
import { removeDuplicates } from "./solution";

describe("Remove Duplicates from Sorted Array", () => {
  it("testcase1", () => {
    const nums = [1, 1, 2];
    const expected = 2;
    const result = removeDuplicates(nums);
    expect(result).toEqual(expected);
    expect(nums).toEqual([1, 2]);
  });

  it("testcase2", () => {
    const nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
    const expected = 5;
    const result = removeDuplicates(nums);
    expect(result).toEqual(expected);
    expect(nums).toEqual([0, 1, 2, 3, 4]);
  });
});
