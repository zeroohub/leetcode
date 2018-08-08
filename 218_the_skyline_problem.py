# -*- coding: utf-8 -*-
from bisect import bisect_left

class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        rights = [(float('inf'), 0)]
        height = 0
        result = []

        for li, ri, h in buildings:
            while li > rights[-1][0]:
                right = rights.pop()
                result.append((right[0], rights[-1][1]))
                height = rights[-1][1]

            if li <= rights[-1][0]:
                if h > height:
                    result.append((li, h))
                    height = h

            idx = bisect_left(list(zip(*rights))[1], h)
            rights.insert(idx, (ri, h))
            i = 0
            while i < idx:
                if rights[i][0] < rights[idx][0]:
                    rights.pop(i)
                    idx -= 1
                else:
                    i += 1

        while len(rights) > 1:
            right = rights.pop()
            result.append((right[0], rights[-1][1]))

        return result

print(Solution().getSkyline([[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]]))
print(Solution().getSkyline([[0,2,3], [2,5,3]]))
