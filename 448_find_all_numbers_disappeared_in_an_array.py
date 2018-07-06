# -*- coding: utf-8 -*-
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        result = set(range(1, len(nums)+1))
        for i in nums:
            result.discard(i)

        return list(result)
