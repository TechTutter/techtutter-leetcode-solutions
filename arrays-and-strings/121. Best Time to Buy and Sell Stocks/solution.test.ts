import { describe, it, expect } from "vitest";
import { maxProfit } from "./solution";
describe("Best Time to Buy and Sell Stocks", () => {
  it("testcase1", () => {
    const prices = [7, 1, 5, 3, 6, 4];
    const expected = 5;
    const result = maxProfit(prices);
    expect(result).toEqual(expected);
  });

  it("testcase2", () => {
    const prices = [7, 6, 4, 3, 1];
    const expected = 0;
    const result = maxProfit(prices);
    expect(result).toEqual(expected);
  });
});
