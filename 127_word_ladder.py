# -*- coding: utf-8 -*-
from copy import copy


class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        queue = []
        word_set = set(wordList)
        try:
            word_set.remove(endWord)
        except KeyError:
            return 0

        queue.append((endWord, 1))

        while queue:
            target, step = queue.pop(0)
            if self.difference(target, beginWord) == 1:
                return step + 1

            for word in word_set.copy():
                if self.difference(word, target) == 1:
                    word_set.remove(word)
                    queue.append((word, step + 1))

        return 0

    def difference(self, w1, w2):
        cnt = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                cnt += 1
        return cnt


from collections import defaultdict
class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        queue = []
        visited = set()
        combine = defaultdict(list)
        if endWord not in wordList:
            return 0

        for word in wordList:
            for i in range(len(beginWord)):
                combine[word[:i] + "*" + word[i+1:]].append(word)

        queue.append((beginWord, 1))

        while queue:
            target, step = queue.pop(0)
            for i in range(len(beginWord)):
                interword = target[:i] + "*" + target[i+1:]
                for word in combine[interword]:
                    if word == endWord:
                        return step + 1

                    if word not in visited:
                        visited.add(word)
                        queue.append((word, step + 1))

                del combine[interword]
        return 0


def test_solution():
    assert Solution().ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]) == 0
    assert Solution().ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log", 'cog']) == 5

test_solution()
