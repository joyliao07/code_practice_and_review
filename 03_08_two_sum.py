# Exercise: Two Sum

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for a in range((i+1), len(nums)):
                added = nums[i] + nums[a]
                if added == target:
                    return [i, a]


############################################
####          TO PRINT SOLUTIONS:       ####
####                                    ####
############################################

nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))
