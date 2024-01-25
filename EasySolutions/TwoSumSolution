"""
Two sum

Given an array of integers [nums] and an integer target, find the indices of two numbers in [nums] that 
add up to target
"""
class TwoSumSolution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        """
        Super brute force, loop through once at index i = 0 and again with index j = 1
        will start at nums[0] and loop through all values at nums[j], if not found,
        start again at nums[1] and nums[j], repeat
        """

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(f"Found solution at indices {i} and {j}")
                    return [i, j]
  
    def twoSumPointer(self, nums: list[int], target: int) -> list[int]:

        """
        Using two pointers, one at beginning and end of list, and depending on nums array being sorted,
        increment / decrement pointer depending on if target is greater than sum of indices (increment left)
        or if target is less than sum of indices (decrement right), pointers will narrow towards the center
        of the array without the use of two for loops
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1

        return []