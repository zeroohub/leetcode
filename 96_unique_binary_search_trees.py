# -*- coding: utf-8 -*-

class Solution(object):
    """
    Fail to solve this myself
    https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)
    """
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0 for i in range(n+1)]
        G[0] = G[1] = 1
        for i in range(2, n+1):
            for r in range(1, i+1):
                G[i] += G[i-r] * G[r-1]

        return G[n]
