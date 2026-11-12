class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0        
        sIntervals = sorted(intervals)
        if len(intervals) < 2:
            return count
        prevEnd = sIntervals[0][1]
        for i in range(len(sIntervals) - 1):
            if sIntervals[i + 1][0] < prevEnd:
                if sIntervals[i + 1][1] < prevEnd:
                    count += 1
                    prevEnd = sIntervals[i + 1][1]
                else:
                    count += 1
            else:
                prevEnd = sIntervals[i + 1][1]
        return count
        