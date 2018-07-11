# -*- coding: utf-8 -*-
class MySolution(object):
    def generateParenthesis(self, n):
        """
        very slow solution took O(2(n-1)n!) time complexity
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        queue = ['()']
        result = set(queue)
        if n == 1:
            return queue
        while len(queue) > 0:
            if len(queue[0]) + 2 > 2*n:
                return queue

            elem = queue.pop(0)
            for x in range(len(elem)):
                new_elem = elem[:x] + '()' + elem[x:]
                if new_elem not in result:
                    result.add(new_elem)
                    queue.append(new_elem)


class Solution2(object):
    def generateParenthesis(self, n):
        """
        use a tree to generate all possible combination, takes minimum time.
        :param n:
        :return:
        """
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []

        def backtrack(S='', left=0, right=0):

            if len(S) == 2 * n:
                ans.append(S)
                return

            if left < n:
                backtrack(S + '(', left + 1, right)

            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()

        return ans
