class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counts = collections.Counter(nums)
        top = counts.most_common(k)
        for x in top:
            result.append(x[0])
        return result