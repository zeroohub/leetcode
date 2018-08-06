# -*- coding: utf-8 -*-
class Solution:
    def minDistance(self, word1, word2):
        """
        DP solution
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for j in range(len(word1)+1)] for i in range(len(word2)+1)]
        for i in range(len(word2) + 1):
            for j in range(len(word1) + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    last = 1 if word1[j-1] != word2[i-1] else 0
                    dp[i][j] = min(last + dp[i-1][j-1], 1 + dp[i][j-1], 1+dp[i-1][j])
        return dp[-1][-1]


class Solution2:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = []
        pre = 0
        for i in range(len(word2) + 1):
            for j in range(len(word1) + 1):
                if i == 0:
                    dp.append(j)
                    pre = j
                elif j == 0:
                    pre = dp[j]
                    dp[j] = i
                else:
                    last = 1 if word1[j-1] != word2[i-1] else 0
                    temp = dp[j]
                    dp[j] = min(1+dp[j], 1+dp[j-1], last+pre)
                    pre = temp

        return dp[-1]

