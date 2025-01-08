#/usr/bin/Python3

"""

Problem:

Given two strings, word1 and word2, merge the strings by adding their letters in alternating order,\
starting with word1. If a string is longer than the other, append the additional letters onto the
merged string.

Approach:

Start with two pointers, i and j, that each begin at index zero of their respective strings. 
Loop over both, condition being while index i is less than length of word 1 or index j less than length of word 2
Append the resulting index to a result empty string
Return 


"""

class solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        res = ""

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                res += word1[i]
                i += 1

            if j < len(word2):
                res += word2[j]
                j += 1

        return res
