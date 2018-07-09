# -*- coding: utf-8 -*-

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = set()

        for i in nums:
            if i in result:
                result.remove(i)
            else:
                result.add(i)

        return result.pop()
