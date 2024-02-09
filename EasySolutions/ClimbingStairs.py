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
where the patterns are not so clear, how would we go about solving this? One way to reduce the time
complexity of solving this recursively is to use a list of no fixed length to map the number of steps present 
(n, the number of stairs present) to the number of methods used to get there (the value mapping).
However, we would have to sum both the current and previous values of the current key index to find
all the possible combinations of one or two steps for however many steps are in the staircase.

Doing this recurisively would be relatively quick and simple for very small values of n, but as
it grows in size, the number of recursive function calls quickly balloons and even a modest n = 20
would take quite a long time, not even discussing n = 50 and above. This is because at each branch of
the decision tree, there are multiple recursive function calls that have previously been calculated, 
and others on top of that that have also previously been calculated, so doing so for each value
even if it was previously found is very time expensive. 

So we create a list, map the known values of 1 and 2, and loop up to the n given, summing the
current and previous value of the keys, and storing them for later use in the method.
"""

class ClimbingStairsSolution:
    def ClimbingStairs(self, n: int) -> int:
        
        if n == 0:
            return(0)
        if n == 1:
            return(1)
        if n == 2:
            return(2)
        
        methods_per_steps = [1, 2]

        for i in range(2, n+1):
            methods_per_steps.append(methods_per_steps[i -1] + methods_per_steps[i - 2])
        return(methods_per_steps[n- 1])

