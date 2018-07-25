# -*- coding: utf-8 -*-
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        TODO
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s.replace('|', '') == '':
            return True

        for idx, word in enumerate(wordDict):
            result = s.replace(word, '|')
            copy = wordDict[:]
            copy.pop(idx)
            if self.wordBreak(result, copy):
                return True

        return False

print(Solution().wordBreak('cbca', ["bc", 'ca']))
