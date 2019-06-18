# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Given nums = [3,2,2,3], val = 3,

# Your function should return length = 2, with the first two elements of nums being 2.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """Runtime 85.60%; Memory 39.55%"""
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i +=1
        return nums

