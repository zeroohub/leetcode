# -*- coding: utf-8 -*-
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        operations = 0
        idx = 0
        while idx < len(nums) - operations:
            if nums[idx] == 0:
                del nums[idx]
                nums.append(0)
                operations += 1
            else:
                idx += 1

