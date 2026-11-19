class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        myHeap = []
        heapq.heapify(myHeap)

        for num in nums:
            freqs[num] += 1
        for key in freqs:
            value = freqs[key]
            if len(myHeap) < k:
                heapq.heappush(myHeap, [value, key])
            else:
                other = heapq.heappop(myHeap)
                if value < other[0]:
                    heapq.heappush(myHeap, other)
                else:
                    heapq.heappush(myHeap, [value, key])
        return [pair[1] for pair in myHeap]