# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """Runtime 15.98%; Memory 94.95%"""
        if len(nums) == 0 or len(nums) == 1:
            return

        for i in reversed(range(len(nums))):
            temp = nums[i:]
            temp.sort(reverse=True)
            if temp == nums[i:]:
                position = i

        if position == 0:
            nums.sort()
            return

        for i in range(position, len(nums)):
            if nums[i] > nums[position - 1]:
                position_2 = i

        nums[position - 1], nums[position_2] = nums[position_2], nums[position - 1]

        temp_2 = nums[position:]
        temp_2.sort()
        nums[position:] = temp_2
        return
