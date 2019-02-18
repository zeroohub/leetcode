# -*- coding: utf-8 -*-
class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        result = 0
        J_set = set(J)
        for i in S:
            if i in J_set:
                result += 1
        return result

print(Solution().numJewelsInStones("aA", "aAAbbbb"))
