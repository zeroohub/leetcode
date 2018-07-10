# -*- coding: utf-8 -*-
class MySolution(object):
    """
    generate all substring, check if palindromic one by one
    time complexity O(n!)
    """

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.palindromic = set()
        counter = 0
        for i in range(len(s) + 1):
            sub = s[:i]
            for x in range(len(sub)):
                counter += int(self.is_palindromic(sub[-(x + 1):]))

        return counter

    def is_palindromic(self, s):
        if len(s) == 1:
            self.palindromic.add(s)
            return True

        start = 0
        end = len(s) - 1

        if len(s) == 2 and s[start] == s[end]:
            self.palindromic.add(s)
            return True

        if s[start] == s[end] and s[start + 1: end] in self.palindromic:
            self.palindromic.add(s)
            return True

        return False


class Solution2(object):
    """
    get all the same char chunks,
    than extend them, to get all the other palindromic
    """
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        # combine same characters into chunks
        cache = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                ans += j - i + 1
                j += 1
            cache.append((i, j - 1))
            i = j

        # for each same character chunk, check left and right
        for left, right in cache:
            left -= 1
            right += 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans


print(Solution2().countSubstrings('aaaa'))
