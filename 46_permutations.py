# -*- coding: utf-8 -*-
class Solution(object):
    """
    iterative solution, can also be done with
    the equivalent recurrent solution
    """
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        queue = [[nums[0]]]

        for n in nums[1:]:
            new_queue = []
            while len(queue) > 0:
                e = queue.pop()
                for i in range(len(e)):
                    new_queue.append(e[:i] + [n] + e[i:])
                new_queue.append(e + [n])
            queue = new_queue

        return queue

