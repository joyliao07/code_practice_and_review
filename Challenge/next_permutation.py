# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 0 or len(nums) == 1:
            return
        
        greater = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > greater:
                greater = nums[i]
        
        if greater == nums[0]:
            nums.sort()
            return
            
        nums.remove(greater)
            
        if len(nums) >= 2:
            nums.insert(1, greater)
        else:
            nums.insert(0, greater)
        
        return





















