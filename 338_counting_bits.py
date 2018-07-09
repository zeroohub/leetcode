# -*- coding: utf-8 -*-
class MySolution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return [self.count_one(n) for n in range(num+1)]


    def count_one(self, integer):
        counter = 0
        while integer > 0:
            integer, mod = divmod(integer, 2)
            counter += mod
        return counter


class Solution2(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        for n in range(1, num+1):
            c = result[n//2]
            if n%2 == 1:
                c += 1
            result.append(c)
        return result


