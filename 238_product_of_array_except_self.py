# -*- coding: utf-8 -*-

class Solution(object):
    """
    fail to find solution without division
    https://leetcode.com/problems/product-of-array-except-self/discuss/147662/One-pass-Java-solution-O(n)-time-O(1)-space
    """
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lnum = len(nums)
        left = right = 1
        result = [1 for i in range(lnum)]

        for i in range(lnum):
            ri = lnum-i-1
            result[i] *= left
            result[ri] *= right
            left *= nums[i]
            right *= nums[ri]
        return result


