class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        length = len(prices)
        max_profit = 0
        while right < length:
            isLess = prices[left] < prices[right]
            if isLess:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return max_profit
        