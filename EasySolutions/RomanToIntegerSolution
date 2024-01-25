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