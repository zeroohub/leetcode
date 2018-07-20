# -*- coding: utf-8 -*-
class Solution(object):
    def canPartition(self, nums):
        """
        TODO
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        left = 0
        right = len(nums)
        outer_sum = 0
        inner_sum = sum(nums)
        for ri in range(right, 0, -1):
            for li in range(left, ri):
                if outer_sum == inner_sum:
                    return True
                inner_sum -= nums[li]
                outer_sum += nums[li]




