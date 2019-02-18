# -*- coding: utf-8 -*-
class Solution:
    def calPoints(self, ops: 'List[str]') -> 'int':
        result = 0
        stack = []
        for o in ops:
            val = self.is_int(o)
            if val is not False:
                result += val
                stack.append(val)
            elif o == '+':
                result += (stack[-1] + stack[-2])
                stack.append(stack[-1] + stack[-2])
            elif o == "D":
                result += stack[-1] * 2
                stack.append(stack[-1] * 2)
            else:
                result -= stack.pop()

        return result

    def is_int(self, s):
        try:
            v = int(s)
            return v
        except ValueError:
            return False
