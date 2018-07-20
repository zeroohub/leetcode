# -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        TODO: don't understand question
        :type nums: List[int]
        :rtype: int
        """
        cache = []  # (length, last)
        max_length = 0
        for n in nums:
            i = 0
            while i < len(cache):
                l, last = cache[i]
                if n >= last:
                    cache[i] = (l+1, n)
                else:
                    max_length = max(max_length, l)
                    del cache[i]
                i += 1
            cache.append((1, n))

        return max_length

