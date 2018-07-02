# -*- coding: utf-8 -*-
class MySolution(object):
    def rob(self, nums):
        """
        another version of classical DP
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ln = len(nums)
        if 1 <= ln < 4:
            odd = 0
            even = 0
            for i in range(ln):
                if i % 2 == 1:
                    even += nums[i]
                else:
                    odd += nums[i]
            return max(odd, even)
        else:
            return max(nums[0] + self.rob(nums[2:]),
                       nums[1] + self.rob(nums[3:]))


class Solution2(object):
    def rob(self, nums):
        """
        classical DP -> three formula:

        f(0) = nums[0]
        f(1) = max(nums[0], nums[1])
        f(n) = max(f(n) + fn(n-2), f(n-1))

        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ln = len(nums)
        if ln == 1:
            return nums[0]
        elif ln == 2:
            return max(nums[0], nums[1])
        else:
            return max(nums[0]+self.rob(nums[2:]), self.rob(nums[1:]))


class Solution3(object):
    def rob(self, nums):
        """
        ultimate optimized DP
        """

        # last: last best result
        # now: current best result
        last, now = 0, 0

        # new best result is the max between (last best + i) and (old now best)
        for i in nums:
            temp = now
            now = max(last+i, temp)
            last = temp

        return now

