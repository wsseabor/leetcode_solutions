"""
Longest common prefix

Given an array of strings, find the longest common prefix of the set of strings, i.e.,
["Flower", "Flee", "Float"] = "fl", if none, return ""

First set an empty prefix string, then a variable for any of the strings in the set, does not matter really which string is chosen because
even if the shortest string is chosen the output would be the max possible length of any strings in the set. I.e., ["Float", "Floatilla"],
float would be the shortest common prefix of both, and it wouldn't be necessary to check the longer string except for matching. 

Loop through the given string chosen, set a char variable for each index (read, character) of the string, then set another loop
to go through the array of strings passed in, if either the index is greater than or equal to the string or the next index char does not match,
return an empty string, otherwise add the char to the prefix string set earlier
"""

class LongestCommonPrefixSolution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        prefix = ''

        firstStr = strs[0]

        for i in range(len(firstStr)):
            char = firstStr[i]
            for string in strs:
                if i >= len(string) or string[i] != char:
                    return prefix
            
            prefix += char

        return prefix