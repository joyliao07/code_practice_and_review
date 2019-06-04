# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()
        self.find_sum(nums, target, 4, [], results)
        return results

    def find_sum(self, nums, target, N, result, results):
        if N > len(nums) or N < 2:
            return
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(nums[l])
                    results.append(nums[r])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(nums) - N + 1):
                if nums[i] * N > target or nums[-1] * N < target:
                    break
                self.find_sum(nums[i+1:], target - nums[i], N-1, result+[nums[i]], results)
