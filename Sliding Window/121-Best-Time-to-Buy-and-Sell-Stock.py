class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=0

        for i in range(1, len(prices)):
            if prices[i]>prices[min_price] and min_price<i:
                max_profit=max(max_profit, prices[i]-prices[min_price])
        
            elif prices[i]<prices[min_price]:
                min_price=i
        
        return max_profit