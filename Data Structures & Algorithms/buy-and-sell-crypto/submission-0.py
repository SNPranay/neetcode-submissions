class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        low, maxDiff = prices[0], 0
        
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                diff = prices[i] - low
                
                if diff > maxDiff:
                    maxDiff = diff
        
        return maxDiff