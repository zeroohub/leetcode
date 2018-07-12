# -*- coding: utf-8 -*-
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for i in nums:
            result += [[i] + r for r in result]
        return result

