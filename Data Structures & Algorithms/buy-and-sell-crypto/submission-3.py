class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        myMax = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                diff = prices[r] - prices[l]
                myMax = max(diff, myMax)
            else:
                l = r
            r += 1
        return myMax