# -*- coding: utf-8 -*-
from collections import defaultdict


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        brute force, O(n^2)
        TODO
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = []
        big = 1
        for i, n in enumerate(nums):
            maxval = 1
            for j in range(i):
                if n > nums[j]:
                    maxval = max(maxval, dp[j]+1)
            big = max(maxval, big)
            dp.append(maxval)

        return big



print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))
