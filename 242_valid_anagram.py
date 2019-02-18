# -*- coding: utf-8 -*-

from collections import defaultdict
class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1

        for c in t:
            if c in cnt:
                cnt[c] -= 1
                if cnt[c] == 0:
                    del cnt[c]
            else:
                return False
        return len(cnt) == 0


print(Solution().isAnagram('anagram', 'anagaram'))
