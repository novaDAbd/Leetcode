class Solution:
    def lowerbound(self, nums: list[int], target: int) -> int:
        ans = len(nums)
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def upperbound(self, nums: list[int], target: int) -> int:
        ans = len(nums)
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        lb = self.lowerbound(nums, target)
        ub = self.upperbound(nums, target)

        if lb == n or nums[lb] != target:
            return [-1, -1]

        return [lb, ub - 1]