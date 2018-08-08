# -*- coding: utf-8 -*-
from heapq import *
from bisect import bisect_left

class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        rights = [(0, float('inf'))]
        height = 0
        result = []

        for li, ri, h in buildings:
            while li > rights[-1][1]:
                right = rights.pop()
                result.append((right[1], rights[-1][0]))
                height = rights[-1][0]

            if li <= rights[-1][1]:
                if h > height:
                    result.append((li, h))
                    height = h

            heappush(rights, (h, ri))

        return result

print(Solution().getSkyline([[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]]))
