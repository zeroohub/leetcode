# -*- coding: utf-8 -*-

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(n):
            rev = [elem + (1 << i) for elem in reversed(result)]
            result += rev

        return result

print(Solution().grayCode(3))
