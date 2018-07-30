# -*- coding: utf-8 -*-

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]

        positive = negative = maxi = nums[0]
        for idx, num in enumerate(nums[1:]):
            np = num * positive
            nn = num * negative
            positive = max(np, nn, num)
            negative = min(np, nn, num)
            maxi = max(maxi, positive)

        return maxi

