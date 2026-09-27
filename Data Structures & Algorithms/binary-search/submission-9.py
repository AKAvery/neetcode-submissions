class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) 
            
        while lower < upper:
            mid = lower + ((upper - lower) // 2)
            if nums[mid] > target:
                upper = mid
            elif nums[mid] <= target:
                lower = mid + 1
        if lower and nums[lower - 1] == target:
            return lower - 1
        else:
            return -1
