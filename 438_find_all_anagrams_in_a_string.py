# -*- coding: utf-8 -*-
from collections import defaultdict


class MySolution(object):
    """
    exceed time limit, time complicity O(M) * O(N)
    """
    def __init__(self):
        self.mapStr = {}

    def buildMap(self, p):
        for i, s in enumerate(p):
            if s not in self.mapStr:
                self.mapStr[s] = i

    def str2Num(self, s):
        arr = [0 for i in range(26)]
        for i in s:
            if i not in self.mapStr:
                return None
            arr[self.mapStr[i]] += 1

        return '#'.join([str(a) for a in arr])


    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        self.buildMap(p)
        target = self.str2Num(p)
        result = []
        for n in range(len(s)-len(p)+1):
            sn = self.str2Num(s[n:n+len(p)])
            if sn and sn == target:
                result.append(n)
        return result


class Solution2(object):
    """
    Sliding window
    """
    def __init__(self):
        self.mapStr = defaultdict(int)


    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        for c in p:
            self.mapStr[c] += 1
        result = []
        diff = len(p)
        start = end = 0
        for end in range(len(p)):
            c = s[end]
            if c in self.mapStr:
                self.mapStr[c] -= 1
                if self.mapStr[c] >= 0:
                    diff -= 1

        if diff == 0:
            result.append(0)

        while end < len(s):
            c = s[start]
            if c in self.mapStr:
                if self.mapStr[c] >= 0:
                    diff += 1
                self.mapStr[c] += 1
            start += 1
            c = s[end]
            if c in self.mapStr:
                self.mapStr[c] -= 1
                if self.mapStr[c] >= 0:
                    diff -= 1

            if diff == 0:
                result.append(start)

            end += 1

        return result

Solution2().findAnagrams('ssssssss', 'ss')
