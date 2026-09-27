class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)
        k = 0
        totalHours = 0
        options = []
        while lower <= upper:
            totalHours = 0
            k = lower + ((upper - lower) // 2)
            for p in piles:
                time = math.ceil(p / k)
                totalHours += time
                if totalHours > h:
                    break
            if totalHours > h:
                lower = k + 1
            else:
                options.append(k)
                upper = k - 1
            print(options)
        if options:
            return min(options)
        else:
            return max(piles)


                