# -*- coding: utf-8 -*-
from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: 'str') -> 'int':
        result = OrderedDict()
        c2i = {}
        for i, c in enumerate(s):
            c2i[c] = i
            if c in result:
                result[c] += 1
            else:
                result[c] = 1

        for c, v in result.items():
            if v == 1:
                return c2i[c]
        return -1

print(Solution().firstUniqChar('leetcode'))
