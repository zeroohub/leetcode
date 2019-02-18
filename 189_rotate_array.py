# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def rotate(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        s = len(nums) - k
        nums.extend(nums[:s])
        for i in range(s):
            nums.pop(0)


class Solution:
    def rotate(self, nums: 'List[int]', k: 'int') -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        last = len(nums) - 1
        self.reverse(nums, 0, last)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, last)


    def reverse(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

