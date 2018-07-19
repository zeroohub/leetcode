# -*- coding: utf-8 -*-
class MySolution(object):
    """
    the reversing of backtracking, not optimized
    """
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

class MySolution2(object):
    """
    backtracking, faster
    """
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        candidates.sort()
        self.backtrack(candidates, target, [], 0)
        return self.result


    def backtrack(self, candidate, target, seq, last):
        if target == 0:
            self.result.append(seq)

        if target < candidate[0]:
            return

        for c in candidate:
            if c < last:
                continue

            self.backtrack(candidate, target - c, seq + [c], c)
