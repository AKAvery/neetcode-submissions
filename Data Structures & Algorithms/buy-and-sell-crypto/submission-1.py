class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        myMin = prices[0]
        j = 0
        myDiff = 0

        while j <= len(prices) - 1:
            if prices[j] <= myMin:
                myMin = prices[j]
                j += 1
                continue
            else:
                print("prices[j]: ", prices[j])
                newDiff = prices[j] - myMin
                print(newDiff)
                myDiff = max(newDiff, myDiff)
                j += 1
      
        return myDiff