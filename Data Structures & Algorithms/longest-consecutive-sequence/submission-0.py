class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0
        longest = 0
       
        for n in nums:
            if n - 1  not in numSet:
                while n + length in numSet:
                    length += 1
            longest = max(length, longest)
            length = 0
        return longest