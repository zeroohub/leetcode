# -*- coding: utf-8 -*-

class Solution(object):
    def coinChange(self, coins, amount):
        """
        DP solution, should also be able to solve with DFS
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            prev = [dp[i-c] for c in coins if i - c >= 0 and dp[i-c] != -1]
            if prev:
                dp[i] = 1 + min(prev)

        return dp[-1]
