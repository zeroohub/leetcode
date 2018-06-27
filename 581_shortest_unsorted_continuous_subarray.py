# -*- coding: utf-8 -*-
import sys

class Solution(object):

    def __init__(self):
        self.small_idx = 0
        self.big_idx = 0
        self.first_disorder_idx = sys.maxsize
        self.current_disorder_idx = -1

    def isAsc(self, idx, n, nums):

        if n < nums[self.small_idx]:
            if self.small_idx < self.first_disorder_idx:
                self.first_disorder_idx = self.small_idx
            self.small_idx = idx
            self.current_disorder_idx = idx
        elif n > nums[self.big_idx]:
            self.big_idx = idx
        elif n < nums[self.big_idx]:
            if self.big_idx < self.first_disorder_idx:
                self.first_disorder_idx = self.big_idx
            self.current_disorder_idx = idx

    def findUnsortedSubarray(self, nums):
        for idx, n in enumerate(nums):
            self.isAsc(idx, n, nums)
        if self.first_disorder_idx == sys.maxsize:
            return 0
        return self.current_disorder_idx - self.first_disorder_idx + 1

print(Solution().findUnsortedSubarray([1,2,4,5,3]))
