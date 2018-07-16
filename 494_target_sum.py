# -*- coding: utf-8 -*-
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        TODO: optimize
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.counter = 0
        self.travel(nums, 0, S)
        return self.counter

    def travel(self, next_num, current_sum, S):
        if not next_num:
            if current_sum == S:
                self.counter += 1
            return

        self.travel(next_num[1:], current_sum + next_num[0], S)
        self.travel(next_num[1:], current_sum - next_num[0], S)
