class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in pair:
                return [pair[difference], i]
            pair[nums[i]] = i
        