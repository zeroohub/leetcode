# -*- coding: utf-8 -*-

class Solution(object):
    """
    Fail to come up solution
    """
    def is_equal(self, s1, s2):
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i] and s2[i] != '.':
                return False
        return True

    def split(self, p):
        result = []
        left = right = 0
        while right < len(p):
            if p[right] == '*':
                result.append(p[left: right+1])
                left = right + 1
            right += 1
        if left != right:
            result.append(p[left: right])
        return result


    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p = self.split(p)
        pi = 0
        while pi < len(p) and s:
            p1 = p[pi]

            if p1[-1] != '*':
                if not (len(s) >= len(p1) and self.is_equal(s[:len(p1)], p1)):
                    return False
                else:
                    s = s[len(p1):]
                    pi += 1
                    continue
            else:
                p1 = p1[:-1]
                if len(p1) > 1:
                    if not (len(s) >= len(p1)-1 and self.is_equal(s[:len(p1)-1], p1[:-1])):
                        return False
                    s = s[len(p1)-1:]
                    p1 = p1[-1]

                while s and self.is_equal(s[0], p1):
                    s = s[1:]

                pi += 1

        return (not bool(s)) and pi == len(p)

class Solution2(object):
    def isMatch(self, text, pattern):
        """
        TODO
        DP solution from:
        https://leetcode.com/problems/regular-expression-matching/solution/
        :param text:
        :param pattern:
        :return:
        """
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
