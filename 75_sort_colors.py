# -*- coding: utf-8 -*-
class Solution(object):
    def sortColors(self, nums):
        """
        quick sort
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.sort(nums, 0, len(nums)-1)

    def sort(self, arr, left, right):
        if right > left:
            pivot_idx = left + (right - left) // 2
            pivot_idx = self.partition(arr, left, right, pivot_idx)
            self.sort(arr, left, pivot_idx-1)
            self.sort(arr, pivot_idx+1, right)

    def partition(self, arr, left, right, pivot_idx):
        pivot_val = arr[pivot_idx]
        arr[right], arr[pivot_idx] = arr[pivot_idx], arr[right]
        store_idx = left
        for i in range(left, right):
            if arr[i] <= pivot_val:
                arr[store_idx], arr[i] = arr[i], arr[store_idx]
                store_idx += 1
        arr[right], arr[store_idx] = arr[store_idx], arr[right]
        return store_idx


class Solution2(object):
    def sortColors(self, nums):
        """
        counting sort
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counter = [0 for i in range(3)]
        for i in nums:
            counter[i] += 1

        p = 0
        for i in range(len(nums)):
            while not counter[p]:
                p += 1
            nums[i] = p
            counter[p] -= 1

