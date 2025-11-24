import { describe, it, expect } from "vitest";
import { maxProfit } from "./solution";

describe("Best Time to Buy and Sell Stocks II", () => {
  it("testcase1", () => {
    const prices = [7, 1, 5, 3, 6, 4];
    const expected = 7;
    const result = maxProfit(prices);
    expect(result).toEqual(expected);
  });

  it("testcase2", () => {
    const prices = [1, 2, 3, 4, 5];
    const expected = 4;
    const result = maxProfit(prices);
    expect(result).toEqual(expected);
  });
});
