import { describe, it, expect } from "vitest";
import { canJump } from "./solution";

describe("Jump Game", () => {
  it("testcase1", () => {
    const nums = [2, 3, 1, 1, 4];
    const expected = true;
    const result = canJump(nums);
    expect(result).toEqual(expected);
  });

  it("testcase2", () => {
    const nums = [3, 2, 1, 0, 4];
    const expected = false;
    const result = canJump(nums);
    expect(result).toEqual(expected);
  });
});
