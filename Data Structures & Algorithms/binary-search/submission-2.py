class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) 
            
        while lower < upper:
            curr = lower + ((upper - lower) // 2)
            if target < nums[curr]:
                upper = curr
            elif target >= nums[curr]:
                lower = curr + 1
        if lower and nums[lower -1] == target:
            return lower - 1
        else: 
            return -1
