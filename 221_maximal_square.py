# -*- coding: utf-8 -*-
class Solution(object):
    def maximalSquare(self, matrix):
        """
        brute force, time exceeded
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = col = 0
        sq = 1
        while row <= len(matrix) - sq:
            col = 0
            while col <= len(matrix[0]) - sq:
                num = sum([sum([int(matrix[j][i]) for i in range(col, col+sq) if i < len(matrix[0])]) for j in range(row, row+sq) if j < len(matrix)])
                if num == sq**2:
                    sq += 1
                else:
                    col += 1
            row += 1
        return (sq - 1) ** 2


class Solution2(object):
    def maximalSquare(self, matrix):
        """
        TODO dp
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = col = 0
        sq = 1
        while row <= len(matrix) - sq:
            col = 0
            while col <= len(matrix[0]) - sq:
                num = sum([sum([int(matrix[j][i]) for i in range(col, col+sq) if i < len(matrix[0])]) for j in range(row, row+sq) if j < len(matrix)])
                if num == sq**2:
                    sq += 1
                else:
                    col += 1
            row += 1
        return (sq - 1) ** 2

