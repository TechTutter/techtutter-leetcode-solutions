import { describe, it, expect } from "vitest";
import { isPalindrome } from "./solution";

describe("Valid Palindrome", () => {
  it("testcase1", () => {
    const s = "A man, a plan, a canal: Panama";
    const expected = true;
    const result = isPalindrome(s);
    expect(result).toEqual(expected);
  });

  it("testcase2", () => {
    const s = "race a car";
    const expected = false;
    const result = isPalindrome(s);
    expect(result).toEqual(expected);
  });

  it("testcase3", () => {
    const s = " ";
    const expected = true;
    const result = isPalindrome(s);
    expect(result).toEqual(expected);
  });
});
