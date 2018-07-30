# -*- coding: utf-8 -*-
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        x = bin(x)[2:]
        xl = len(x)
        y = bin(y)[2:]
        yl = len(y)
        if yl > xl:
            ld = yl - xl
            one = sum([1 for i in y[:ld] if i == '1'])
            y = y[ld:]
        else:
            ld = xl - yl
            one = sum([1 for i in x[:ld] if i == '1'])
            x = x[ld:]

        diff = sum([1 for i in range(len(x)) if x[i] != y[i]])
        return one + diff

class Solution2(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')

