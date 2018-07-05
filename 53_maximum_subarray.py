# -*- coding: utf-8 -*-

class Solution(object):
    """
    three formula:
    f(0) = nums[0]
    f(1) = max(nums[1], nums[1] + nums[0])
    f(n) = max(nums[n], nums[n] + f(n-1))
    """

    def maxSubArray(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        real_max = nums[0]
        maximum = 0
        for i in nums:
            maximum = max(i, i + maximum)
            if maximum > real_max:
                real_max = maximum
        return real_max
