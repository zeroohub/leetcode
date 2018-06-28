# -*- coding: utf-8 -*-

class MySolution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        snums = {}
        for i, n in enumerate(nums):
            if snums:
                l = (target - n)
                if l in snums:
                    return i, snums[l]
            snums[n] = i



class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        snums = list(enumerate(nums))
        snums.sort(key=lambda a: a[1])
        li = 0
        ri = len(snums)-1
        while li < ri:
            cr = snums[li][1] + snums[ri][1]
            if cr == target:
                return [snums[li][0], snums[ri][0]]
            elif cr > target:
                ri -= 1
            elif cr < target:
                li += 1


print(Solution2().twoSum([2,7,11,15], 9))
