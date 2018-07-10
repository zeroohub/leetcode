# -*- coding: utf-8 -*-
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # TODO
        pair = '()'
        left = '('
        right = ')'
        result = [pair * n]

