# -*- coding: utf-8 -*-
class Solution(object):
    def longestValidParentheses(self, s):
        """
        DP solution
        :type s: str
        :rtype: int
        """
        dp = [0]
        max_val = 0
        for idx in range(1, len(s)):
            if s[idx] == '(':
                dp.append(0)
            elif s[idx] == ')':
                if s[idx-1] == '(':
                    dp.append(dp[idx-2] + 2)
                elif s[idx-1] == ')':
                    if idx-dp[idx-1]-1 == -1:
                        dp.append(0)
                    elif s[idx-dp[idx-1]-1] == '(':
                        pre = 0 if idx-dp[idx-1] - 2 == -1 else dp[idx-dp[idx-1] - 2]
                        dp.append(pre + dp[idx-1] + 2)
                    else:
                        dp.append(0)

            max_val = max(dp[-1], max_val)
        return max_val


class Solution2(object):
    def longestValidParentheses(self, s):
        """
        https://leetcode.com/problems/longest-valid-parentheses/solution/
        :param s:
        :return:
        """
        result = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    result = max(result, i - stack[-1])

        return result


assert Solution2().longestValidParentheses("()(()") == 2
assert Solution2().longestValidParentheses("(()") == 2
assert Solution2().longestValidParentheses(")()())") == 4
assert Solution2().longestValidParentheses("()(())") == 6
assert Solution2().longestValidParentheses(")()())()()(") == 4
assert Solution2().longestValidParentheses("(()(((()") == 2
assert Solution2().longestValidParentheses("(()())") == 6
