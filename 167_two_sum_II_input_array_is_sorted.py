# -*- coding: utf-8 -*-
from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        m_num = defaultdict(list)
        for idx, num in enumerate(numbers):
            m_num[num].append(idx)

        for num in numbers:
            cut = target - num
            if cut in m_num:
                if cut == num:
                    if len(m_num[cut]) == 2:
                        return [n+1 for n in m_num[cut]]
                elif cut > num:
                    return [m_num[num][0]+1, m_num[cut][0]+1]
                else:
                    break

        return []


class Solution2:
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        left = 0
        right = len(numbers) - 1
        while left < right:
            result = numbers[left] + numbers[right]
            if result == target:
                return [left+1, right+1]
            elif result > target:
                right -= 1
            else:
                left += 1
        return []
print(Solution().twoSum([0 ,0, 3, 4], 0))
