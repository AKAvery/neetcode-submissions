class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        myHeap = []
        for num in nums:
            freqs[num] += 1
        for key in freqs:
            value = freqs[key]
            if len(myHeap) < k:
                heapq.heappush(myHeap, [value, key])
            else:
                if value > myHeap[0][0]:
                    heapq.heappop(myHeap)
                    heapq.heappush(myHeap, [value, key])
        return [pair[1] for pair in myHeap]