# -*- coding: utf-8 -*-
from collections import defaultdict


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        TODO: optimize
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.counter = 0
        self.travel(nums, 0, S)
        return self.counter

    def travel(self, next_num, current_sum, S):
        if not next_num:
            if current_sum == S:
                self.counter += 1
            return

        self.travel(next_num[1:], current_sum + next_num[0], S)
        self.travel(next_num[1:], current_sum - next_num[0], S)


class Solution2(object):
    def findTargetSumWays(self, nums, S):
        """
        add memo
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.cache = {}
        return self.travel(nums, 0,  0, S)

    def travel(self, nums, i, current_sum, S):
        if i == len(nums):
            if current_sum == S:
                return 1
            return 0

        if (i, current_sum) in self.cache:
            return self.cache[(i, current_sum)]
        add = self.travel(nums, i+1, current_sum + nums[i], S)
        sub = self.travel(nums, i+1, current_sum - nums[i], S)
        self.cache[(i, current_sum)] = add + sub
        return self.cache[(i, current_sum)]



class Solution3(object):
    """
    dp solution
    """
    def findTargetSumWays(self, nums, target):
        dp = [0 for i in range(2001)]
        dp[nums[0] + 1000] += 1
        dp[-nums[0] + 1000] += 1

        for n in nums[1:]:
            next_dp = [0 for i in range(2001)]
            for s in range(-1000, 1001):
                if dp[s+1000] > 0:
                    next_dp[s+1000+n] += dp[s+1000]
                    next_dp[s+1000-n] += dp[s+1000]

            dp = next_dp

        return 0 if target > 1000 else dp[target + 1000]



class Solution4(object):
    """
    dp solution
    """

    def findTargetSumWays(self, nums, target):
        dp = defaultdict(int)
        dp[nums[0]] += 1
        dp[-nums[0]] += 1

        for n in nums[1:]:
            next_dp = defaultdict(int)
            for s in dp:
                next_dp[s+n] += dp[s]
                next_dp[s-n] += dp[s]
            dp = next_dp

        return dp[target]


print(Solution4().findTargetSumWays([1, 1, 1, 1, 1], 3))
