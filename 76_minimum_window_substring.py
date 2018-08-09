# -*- coding: utf-8 -*-
from collections import Counter

class Solution:
    def minWindow(self, s, t):
        """
        TODO find another way to mark, this way is stupid
        :param s:
        :param t:
        :return:
        """
        left = Counter(t)
        diff = len(t)
        start = 0
        result = (0, 0)
        for end in range(1, len(s)+1):
            if left[s[end-1]] > 0:
                diff -= 1
            left[s[end-1]] -= 1
            if diff == 0:
                while start < end and left[s[start]] < 0:
                    left[s[start]] += 1
                    start += 1
                if result == (0, 0) or end - start < result[1] - result[0]:
                    result = (start, end)

        return s[result[0]:result[1]]




