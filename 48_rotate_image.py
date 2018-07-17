# -*- coding: utf-8 -*-
class Solution(object):
    def rotate(self, matrix):
        """
        good solution from this
        https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        matrix.reverse()
        lm = len(matrix)
        for r in range(lm):
            for c in range(r+1, lm):
                temp = matrix[c][r]
                matrix[c][r] = matrix[r][c]
                matrix[r][c] = temp
