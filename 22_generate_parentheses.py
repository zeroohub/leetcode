# -*- coding: utf-8 -*-
class Solution(object):
    def generateParenthesis(self, n):
        """
        very slow solution took O( )
        TODO
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


print(Solution().generateParenthesis(3))
