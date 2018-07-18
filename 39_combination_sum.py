# -*- coding: utf-8 -*-
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = [[] for i in range(candidates[-1]+1)]
        for idx in range(candidates[0], len(result)):
            for c in candidates:
                if idx == c:
                    result[idx].append({c})
                elif idx > c:
                    for i in result[idx-c]:
                        for j in result[c]:
                            result[idx].append(i + j)
                else:
                    break
        return result


print(Solution().combinationSum([2, 3, 6, 7], 7))


