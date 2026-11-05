class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = defaultdict(int)

        for num in nums:
            curr = counts[num]
            counts[num] = curr + 1
            if counts[num] > 1:
                return num