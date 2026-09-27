class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower = 0
        upper = len(nums) - 1
        m = nums[0]
        while lower <= upper:
            mid = lower + ((upper - lower) // 2)
            print("mid: ", mid)
            if nums[mid] < m:
                m = nums[mid]
                print("m: ", m)
            if nums[mid] < nums[upper] and nums[mid] < nums[lower]:
                if nums[mid - 1] > nums[mid]:
                    return nums[mid]
                else:
                    upper = mid - 1
            elif nums[upper] < nums[lower]:
                    lower = mid + 1
            else:
                upper = mid - 1
        return m