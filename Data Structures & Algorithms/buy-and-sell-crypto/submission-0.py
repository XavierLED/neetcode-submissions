class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], 0
        profit = 0

        for i, p in enumerate(prices):
            if prices[i] < buy:
                buy = prices[i]
                sell = 0

            else:
                sell = prices[i]    
            
            if profit < (sell - buy):
                profit = sell - buy
        return profit
