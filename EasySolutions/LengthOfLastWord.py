#!usr/bin/env python3

"""
Length of last word

Given an input string, find the length of the last word in the string. Ex.:
"Hello World"
"  fly  me to the   moon  "

Given some input string with a lot of extra white space, we first strip the string of extra beginning 
and trailing whitespace, then begin a loop that starts at the end of the string and reads in reverse,
iterating a counter as we go until whitespace is found, denoting the beginning of a word, break the loop
and return the iterated count variable
"""

class LengthOfLastWordSolution():
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.strip()
        count = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            count += 1

        return count
