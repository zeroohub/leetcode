# -*- coding: utf-8 -*-
class Solution(object):
    """
    fail to find solution, not fully understand solution
    TODO
    http://keithschwarz.com/interesting/code/?dir=find-duplicate
    https://leetcode.com/problems/find-the-duplicate-number/solution/
    """

    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1


