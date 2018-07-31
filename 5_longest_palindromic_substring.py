# -*- coding: utf-8 -*-

class Solution(object):
    def longestPalindrome(self, s):
        """
        DP solution in O(n^2) time

        TODO better solution in O(n) time
        https://articles.leetcode.com/longest-palindromic-substring-part-ii/
        https://www.felix021.com/blog/read.php?2040

        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        found = set()
        maxi_sub = s[0]
        maxi_len = 1
        for idx, char in enumerate(s):
            for j in range(idx):
                if char == s[j] and ((j == idx - 1) or (j+1, idx-1) in found):
                    if idx-j+1 > maxi_len:
                        maxi_sub = s[j:idx+1]
                        maxi_len = idx-j+1
                    found.add((j, idx))

            found.add((idx, idx))

        return maxi_sub
