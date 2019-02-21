# -*- coding: utf-8 -*-
from collections import Counter
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        cnt = Counter(S)
        length = 0
        pending = {}
        result = []
        for char in S:
            length += 1
            pending[char] = True
            cnt[char] -= 1
            if cnt[char] == 0:
                del pending[char]
                if len(pending) == 0:
                    result.append(length)
                    length = 0
        return result




def test_solution():
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]

test_solution()
