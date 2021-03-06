# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Given nums = [3,2,2,3], val = 3,

# Your function should return length = 2, with the first two elements of nums being 2.

class Solution:
    def removeElement_1(self, nums: List[int], val: int) -> int:
        """Runtime 85.60%; Memory 39.55%"""
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i +=1
        return nums

    def removeElement_2(self, nums: List[int], val: int) -> int:
        """Runtime 55.93%; Memory 42.85%"""
        while val in nums:
            nums.remove(val)
        return nums

    def removeElement_3(self, nums: List[int], val: int) -> int:
        nums.sort()
        removed = False
        i = 0
        while i < len(nums) and removed is False:
            while i < len(nums):
                if nums[i] == val:
                    nums.remove(nums[i])
                    removed = True
            i += 1
        return nums

    def removeElement_4(self, nums: List[int], val: int) -> int:
        """Return only the length of nums. Runtime 84%; Memory 17%"""
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j








