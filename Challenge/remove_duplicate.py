# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

class Solution:
    def removeDuplicates_1(self, nums: List[int]) -> int:
        """Runtime 5.04%; Memory 43.35%"""
        if len(nums) == 0:
            return
        check = []
        i = 0

        while i < len(nums):
            if nums[i] not in check:
                check.append(nums[i])
                i += 1
            else:
                nums.remove(nums[i])

        return len(nums)

    def removeDuplicates_2(self, nums: List[int]) -> int:
        """Runtime 8.79%; Memory 79.88%"""
        if len(nums) == 0:
            return
        i = 0

        while i+1 < len(nums):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
            else:
                i += 1
       
        return len(nums)














