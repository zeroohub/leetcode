# -*- coding: utf-8 -*-
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_num = len(matrix)
        col_num = len(matrix[0])
        row_mark = [False] * row_num
        col_mark = [False] * col_num
        for row in range(row_num):
            for col in range(col_num):
                if matrix[row][col] == 0:
                    if not row_mark[row]:
                        row_mark[row] = True
                    if not col_mark[col]:
                        col_mark[col] = True
        for row in range(row_num):
            if row_mark[row]:
                matrix[row][:] = [0] * col_num
        for col in range(col_num):
            if col_mark[col]:
                for i in range(row_num):
                    matrix[i][col] = 0


Solution().setZeroes([[0]])
