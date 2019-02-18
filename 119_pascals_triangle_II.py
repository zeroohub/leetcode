# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        result = [1] + [0] * rowIndex
        for i in range(1, rowIndex + 1):
            last_val = 0
            for j in range(i + 1):
                temp = result[j]
                result[j] += last_val
                last_val = temp

        return result

for i in [1, 2, 3, 4, 5]:
    print(Solution().getRow(i))
