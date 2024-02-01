"""
Climbing stairs

You are climbing a staircase which takes n steps to reach the top.
Each time you can either climb one or two steps. How many distinct ways
can you reach the top of the staircase?

Breaking this down into component parts, for base cases, if n = 1, there is only one way to climb the
staircase. As n = 2, there are two ways, 1 + 1 or 2. As n = 3, the problem space becomes decidely
more complex as n increases, giving 1 + 1 + 1, 1 + 2, 2 + 1, giving three solutions. 
One further, as n = 4, the solution gives 1 + 1 + 1 + 1, 2 + 2, 1 + 1 + 2, 1 + 2 + 1, 2 + 1 + 1 
for five solutions.

Okay, that's great, even if the underlying pattern is a fibonacci sequence, in problems like this
where the patterns are not so clear, how would we go about solving this? 



"""

class ClimbingStairsSolution:
    def ClimbingStairs(self, n: int) -> int:
        pass