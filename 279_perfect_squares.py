# -*- coding: utf-8 -*-
from math import sqrt

class MySolution(object):
    """
    too slow, backtrack with memo
    """
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cache = {}
        return self.backtrack(n, int(sqrt(n)))

    def backtrack(self, num, end):
        if (num, end) in self.cache:
            return self.cache[(num, end)]

        if num < 4:
            return num
        short = num
        while end > 1:
            if end*end <= num:
                short = min(short, self.backtrack(num - end*end, end))
                end -= 1
            else:
                end = int(sqrt(num))
        self.cache[(num, end)] = short + 1
        return short + 1


class MySolution2(object):
    """
    DP solution
    """
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]
        for i in range(n+1):
            if i < 4:
                dp.append(i)
                continue

            small = i
            for j in range(int(sqrt(i)), 1, -1):
                small = min(small, dp[i-j*j] + 1)
                if small == 1:
                    break

            dp.append(small)
        return dp[n]


class Solution3(object):
    """
    same DP, just take advantage of static variable
    """
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            result = n
            end = int(len(dp) ** 0.5 + 1)
            for i in range(1, end):
                result = min(result, dp[-i * i])
            result += 1
            dp += result,
        return dp[n]
