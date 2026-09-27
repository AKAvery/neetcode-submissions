class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while lower <= upper:
            mid = lower + ((upper - lower) // 2)
            print("lower: ", lower, " upper: ", upper, " mid: ", mid)
            if nums[lower] == target:
                return lower
            elif nums[upper] == target:
                return upper
            elif nums[mid] == target:
                return mid
            elif nums[lower] <= nums[mid]:
                if target > nums[mid] or target < nums[lower]:
                    lower = mid + 1
                else:
                    upper = mid - 1
            else: 
                if target < nums[mid] or target > nums[upper]:
                    upper = mid - 1
                else:
                    lower = mid + 1


        return -1
            
