class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        myMax = 0
        curr = 0
        while i < j:
            h1 = heights[i]
            h2 = heights[j]
            minH = min(h1, h2)
            diff = j - i 
            total = minH * diff
            if total > myMax:
                myMax = total
            if h1 >= h2:
                j -= 1
            else:
                i += 1
        return myMax