# -*- coding: utf-8 -*-

class Solution(object):
    num2char = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        result = ['']

        for d in digits:
            next_result = []
            for c in self.num2char[d]:
                for r in result:
                    next_result.append(r+c)
            result = next_result

        return result

print(Solution().letterCombinations('23'))
