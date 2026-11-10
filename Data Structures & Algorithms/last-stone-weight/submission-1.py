import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneMaxHeap = []
        for stone in stones:
            inverted = -stone
            heapq.heappush(stoneMaxHeap, inverted)
        print(stoneMaxHeap)
        while len(stoneMaxHeap) > 1:
            x, y = heapq.heappop(stoneMaxHeap), heapq.heappop(stoneMaxHeap)
            
            if x != y:
                z = abs(y - x)
                z = -z
                heapq.heappush(stoneMaxHeap, z)
                
            print(stoneMaxHeap)

        if stoneMaxHeap:
            return -stoneMaxHeap[0]
        return 0