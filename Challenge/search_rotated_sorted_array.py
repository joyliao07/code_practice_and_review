# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

class Solution:
    def search_1(self, nums: List[int], target: int) -> int:
        """Runtime 15.85%; Memory 20.19%"""
        for i in range(len(nums)):
            if nums[i] == target:
                return i         
        return -1


    def search_2(self, nums: List[int], target: int) -> int:
        """Runtime 94.04%; Memory 97.5%"""
        if len(nums) == 0:
            return -1

        if target >= nums[0]:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i    
        else:
            if target > nums[-1]:
                return -1
            for i in range(len(nums) -1, -1, -1):
                if nums[i] == target:
                    return i     
        return -1
