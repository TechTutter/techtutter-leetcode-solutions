import { describe, it, expect } from "vitest";
import { majorityElement, majorityElement2 } from "./solution";

describe("Majority Element", () => {
  it("testcase1", () => {
    const nums = [3, 2, 3];
    const expected = 3;
    const result = majorityElement(nums);
    const result2 = majorityElement2(nums);
    expect(result).toEqual(expected);
    expect(result2).toEqual(expected);
  });

  it("testcase2", () => {
    const nums = [2, 2, 1, 1, 1, 2, 2];
    const expected = 2;
    const result = majorityElement(nums);
    const result2 = majorityElement2(nums);
    expect(result).toEqual(expected);
    expect(result2).toEqual(expected);
  });
});
