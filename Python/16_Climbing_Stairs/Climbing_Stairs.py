class Solution(object):
    def climbStairs(self, N):
        """
        :type n: int
        :rtype: int
        """
        if N <= 1:
            return 1
        prev_prev, prev, ways = 1, 1, 0
        for i in range(2, N+1):
            ways = prev + prev_prev
            prev_prev, prev = prev, ways
        return ways
    