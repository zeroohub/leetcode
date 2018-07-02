# -*- coding: utf-8 -*-

class Solution(object):
    """
    TODO: DP算法
    """
    def maxSubArray(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        end = 0
        start = 0
        big = nums[0]
        current = 0
        for i, n in enumerate(nums):
            current += n
            if current > big:
                big = current
                end = i

        current = big
        for i in range(end):
            current -= nums[i]
            if current > big:
                big = current
                start = i

        return big


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
