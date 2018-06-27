# -*- coding: utf-8 -*-
class MySolution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        rnums = nums[:]
        c1 = 0
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                c1 += 1
                nums[i+1] = nums[i]
            if c1 > 1:
                break

        c2 = 0
        for i in range(len(rnums) - 1, 0, -1):
            if rnums[i-1] > rnums[i]:
                c2 += 1
                rnums[i-1] = rnums[i]
            if c2 > 1:
                break

        return c2 <= 1 or c1 <= 1
