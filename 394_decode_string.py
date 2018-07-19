# -*- coding: utf-8 -*-
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        open_stack = []
        for char in s:
            lstack = len(stack)
            if char == ']':
                repeat_unit = stack[open_stack[-1]+1:]
                stack = stack[:open_stack.pop()]
                repeat_times = ''
                while stack and stack[-1].isdigit():
                    repeat_times = stack.pop() + repeat_times
                stack += repeat_unit * int(repeat_times)
            else:
                if char == '[':
                    open_stack.append(lstack)
                stack.append(char)

        return ''.join(stack)


