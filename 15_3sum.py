# -*- coding: utf-8 -*-

class Solution(object):
    def threeSum(self, nums):
        """
        TODO find way to remove duplicate
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.dfs(nums, 3, 0)

    def dfs(self, nums, left, target):
        if left == 1:
            return [[n] for n in nums if n == target]

        result = []
        scaned = set()
        for idx, n in enumerate(nums):
            if n not in scaned:
                result += [r + [n] for r in self.dfs(nums[idx+1:], left - 1, target-n)]
                scaned.add(n)
        return result

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
