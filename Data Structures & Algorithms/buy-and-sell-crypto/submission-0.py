class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_so_far = 0
        for r, price in enumerate(prices):
            if price < prices[l]:
                l = r
            cur_profit = price - prices[l]

            max_so_far = max(max_so_far,cur_profit)

        return max_so_far
