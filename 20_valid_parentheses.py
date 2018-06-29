# -*- coding: utf-8 -*-

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            elif stack and brackets[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return not stack
