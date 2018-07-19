# -*- coding: utf-8 -*-

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        TODO: check this
        https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60294/Solution-explained
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]
