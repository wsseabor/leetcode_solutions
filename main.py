#!/usr/bin/env python3

"""
Leetcode examples:

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
    
"""
Roman to integer

Given a roman integer, convert the given string of roman numerals to an integer.
Roman numerals are given as (I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)

III would return 3
VIIII would return 9
However for something like IV, it would not be six because if one numeral is less than its corresponding
value to its right, the whole result is decremented by that very value in the first ordinal spot, 
and this can only occur once as there cannot be more than less smaller numeral to the left of a greater one
"""

class RomanSolution:
    def romanToInteger(self, s: str) -> int:

        """
        Define a dictionary of given roman numerals (keys) with their corresponding interger values (value)

        Declare a result variable of zero (our return value as well)

        Loop through the string given it's length

        If the given string is only one character, just maps to the given k, v in the dict, base case

        If the given string is greater than one character and the digit after the current index is greater
        than the previous, decrement the previous numeral from the current one

        Else add the current index to the result
        """

        romans = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

        result = 0

        for i in range(len(s)):
            if i + 1 < len(s) and romans[s[i]] < romans[s[i + 1]]:
                result -= romans[s[i]]
            else:
                result += romans[s[i]]

        return result

