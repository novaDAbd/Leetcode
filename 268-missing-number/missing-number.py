class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        
        sum = int((n*(n+1)/2))
        a=0
        for i in nums:
            a=a+i
        
        missing=sum-a
        return missing