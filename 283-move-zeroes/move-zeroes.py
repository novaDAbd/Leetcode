class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_ptr = 0

        for read_ptr in range(len(nums)):
            if nums[read_ptr] != 0:
                # Swap non-zero element to the write_ptr index
                nums[write_ptr], nums[read_ptr] = nums[read_ptr], nums[write_ptr]
                write_ptr += 1