# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()
        self.find_sum(nums, target, N, [], results)
        return results


    def find_sum(self, nums, target, N, result, results):
        if N < len(nums) or N < 2:
            return
        if N == 2:
            # find the pair



        else:
            for i in range(len(nums) - N + 1):
                if num[i] * N > target or num[-1] * N < target:
                    break
                self.find_sum(nums[i+1:], target - num[i], N-1, result+[num[i]], results)
