# -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0

        chars = {}
        max_len = 0
        for idx, char in enumerate(s):
            if char not in chars:
                max_len = max(max_len, idx - start + 1)
            else:
                if chars[char] >= start:
                    start = chars[char] + 1
                else:
                    max_len = max(max_len, idx - start + 1)
            chars[char] = idx

        return max_len

print(Solution().lengthOfLongestSubstring("abcabcbb"))
