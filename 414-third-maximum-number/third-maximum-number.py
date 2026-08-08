class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums1=set(nums)
        if len(nums1)>=3:
            for i in range(0,3):
                i=max(nums1)
                nums1.remove(i)

        else:
            i=max(nums1)
        return i

    