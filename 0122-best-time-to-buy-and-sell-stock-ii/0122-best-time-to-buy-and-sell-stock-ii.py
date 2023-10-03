class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = 0 
        p=0
        while i<n-1:
            if prices[i]<prices[i+1]:
                p+=(prices[i+1]-prices[i])
            i+=1
        return p 
        