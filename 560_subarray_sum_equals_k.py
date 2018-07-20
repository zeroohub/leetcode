# -*- coding: utf-8 -*-
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
