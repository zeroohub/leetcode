# -*- coding: utf-8 -*-
from data_structure import *
from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma = len(nums) / 2

        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
            if counter[i] > ma:
                return i


