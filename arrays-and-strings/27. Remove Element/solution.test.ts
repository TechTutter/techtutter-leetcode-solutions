import { describe, it, expect } from "vitest";
import { removeElement } from "./solution";

describe("Remove Element", () => {
  it("testcase1", () => {
    const nums = [3, 2, 2, 3];
    const val = 3;
    const expected = 2;
    const result = removeElement(nums, val);
    expect(result).toEqual(expected);
    expect(nums).toEqual([2, 2]);
  });

  it("testcase2", () => {
    const nums = [0, 1, 2, 2, 3, 0, 4, 2];
    const val = 2;
    const expected = 5;
    const result = removeElement(nums, val);
    expect(result).toEqual(expected);
    expect(nums).toEqual([0, 1, 4, 0, 3]);
  });
});
