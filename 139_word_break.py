# -*- coding: utf-8 -*-
class MySolution(object):
    def wordBreak(self, s, wordDict):
        """
        DFS should work
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict.sort(key=lambda w: len(w), reverse=True)
        return self.dfs(s, wordDict)

    def dfs(self, s, words):
        if not s:
            return True
        for w in words:
            if s.startswith(w) and self.dfs(s[len(w):], words):
                return True
        return False


class Solution(object):
    def wordBreak(self, s, words):
        """
        DP solution
        https://leetcode.com/problems/word-break/discuss/43788/4-lines-in-Python
        https://leetcode.com/problems/word-break/discuss/43808/Simple-DP-solution-in-Python-with-description
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [True]
        max_len = max(map(len,words+['']))
        words = set(words)
        for i in range(1, len(s)+1):
            dp.append(any(dp[j] and s[j:i] in words for j in range(max(0, i-max_len), i)))
        return dp[-1]
