# -*- coding: utf-8 -*-
import sys


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        self.begin = beginWord
        self.result = 0
        self.dfs(endWord, wordset, 1)
        return self.result

    def dfs(self, target, wordset, depth):
        if len(wordset) == 0 and self.difference(target, self.begin) == 1:
            self.result = min(self.result, depth + 1) if self.result != 0 else depth + 1

        temp = []
        for word in wordset:
            if self.difference(word, target) == 1:
                temp.append(word)

        for word in temp:
            wordset.remove(word)
        for word in temp:
            self.dfs(word, wordset, depth + 1)

    def difference(self, w1, w2):
        cnt = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                cnt += 1
        return cnt

def test_solution():
    assert Solution().ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"]) == 5

test_solution()
