function maxProfit(prices: number[]): number {
  let minPrice = 10e9;
  let maxProfit = 0;
  let profit = 0;

  for (const p of prices) {
    if (p < minPrice) minPrice = p;
    profit = p - minPrice;
    if (profit > maxProfit) maxProfit = profit;
  }
  return maxProfit;
}

export { maxProfit };
