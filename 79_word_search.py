# -*- coding: utf-8 -*-

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.dfs(word, i, j, board):
                    return True

        return False

    def dfs(self, word, i, j, board):
        if not word:
            return True

        if not (0 <= i < len(board) and 0 <= j < len(board[i])):
            return False

        if word[0] != board[i][j]:
            return False

        temp = board[i][j]
        board[i][j] = '#'

        for ni, nj in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
            if self.dfs(word[1:], ni, nj, board):
                return True
        board[i][j] = temp
        return False


print(Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]]
,"AAB"))
