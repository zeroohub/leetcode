# -*- coding: utf-8 -*-

class MySolution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        total = len(candies)
        sis_max = total // 2
        kinds = len(set(candies))
        if kinds > sis_max:
            return sis_max
        return kinds


class Solution2(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        total = len(candies)
        sis_max = total // 2
        count = 1
        candies.sort()
        for idx, c in enumerate(candies[:-1]):
            if candies[idx+1] > c:
                count += 1
                if count > sis_max:
                    return sis_max
        return count
