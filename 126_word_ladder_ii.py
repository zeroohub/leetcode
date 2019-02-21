# -*- coding: utf-8 -*-
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        if endWord not in wordList:
            return 0

        visted = set()
        combo = defaultdict(list)
        muts = defaultdict(list)
        L = len(beginWord)
        for word in [beginWord] + wordList:
            muts[word] = [word[:i] + "*" + word[i+1:] for i in range(L)]
            for mut in muts[word]:
                combo[mut].append(word)

        queue = [(beginWord, 1)]

        while queue:
            word, step = queue.pop(0)
            if word == endWord:
                return step
            for mut in muts[word]:
                for nword in combo[mut]:
                    if nword in visted:
                        continue
                    visted.add(nword)
                    queue.append((nword, step + 1))

        return 0

print(Solution().ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
