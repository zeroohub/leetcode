# -*- coding: utf-8 -*-
from functools import reduce


class MySolution(object):
    def chunk_list(self, nums, n):
        for i in range(0, len(nums), n):
            yield nums[i: i + n]

    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        new_nums = reduce(lambda a, b: a + b, nums)
        if r * c != len(new_nums):
            return nums

        return list(self.chunk_list(new_nums, c))


class Solution2(object):

    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nr = len(nums)
        nc = len(nums[0]) if nr else 0
        if nc * nr != r * c:
            return nums

        result = [range(c) for i in range(r)]
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                result[count // c][count % c] = nums[i][j]
                count += 1

        return result
