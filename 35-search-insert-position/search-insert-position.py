class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        ans = len(nums)
        high = len(nums) - 1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid -1
            else:
                low = mid+1
        return ans
        