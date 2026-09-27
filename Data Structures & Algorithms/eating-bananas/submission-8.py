class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)
        m = 0
        k = 0
        totalHours = 0
        options = []


        while lower <= upper:
            totalHours = 0
            k = lower + ((upper - lower) // 2)
            print("k: ", k)
            for p in piles:
                time = math.ceil(p / k)
                totalHours += time
                print(totalHours)
                if totalHours > h:
                    break
            if totalHours > h:
                print("in totalHours > h")
                lower = k + 1
            else:
                print("in totalHours < h")
                options.append(k)
                upper = k - 1
            print(options)
        if options:
            return min(options)
        else:
            return max(piles)


                