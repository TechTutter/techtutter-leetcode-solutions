function maxProfit(prices: number[]): number {
  let minPrice = Infinity;
  let cumulativeProfit = 0;
  let maxCurrentProfit = 0;
  let currentProfit = 0;

  for (const p of prices) {
    if (p < minPrice) minPrice = p;
    currentProfit = p - minPrice;
    if (currentProfit > 0) {
      cumulativeProfit += currentProfit;
      minPrice = p;
    }
  }
  return cumulativeProfit;
}

export { maxProfit };
