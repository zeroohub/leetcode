# -*- coding: utf-8 -*-
from collections import defaultdict


class MySolution(object):
    def subarraySum(self, nums, k):
        """
        brute force, consider all possible sub array, time exceeded
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        current_sums = []
        result = 0
        for n in nums:
            next_sums = [n]
            if n == k:
                result += 1
            for s in current_sums:
                sn = s + n
                if sn == k:
                    result += 1
                next_sums.append(sn)
            current_sums = next_sums
        return result


class MySolution2(object):
    def subarraySum(self, nums, k):
        count = 0
        for start in range(len(nums)):
            S = 0
            for end in range(start, len(nums)):
                S += nums[end]
                if S == k:
                    count += 1

        return count

class Solution(object):
    def subarraySum(self, nums, k):
        cur_sum = defaultdict(int, {0:1})
        nsum = 0
        count = 0
        for n in nums:
            nsum += n
            if nsum - k in cur_sum:
                count += cur_sum[nsum - k]
            cur_sum[nsum] += 1
        return count



print(Solution().subarraySum([1, 1, 1], 2))
