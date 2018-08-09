# -*- coding: utf-8 -*-
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums_set = set(nums)
        for n in nums_set:
            if n - 1 not in nums_set:
                counter = 1
                while n + 1 in nums_set:
                    counter += 1
                    n += 1

                result = max(result, counter)

        return result
