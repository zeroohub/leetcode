# -*- coding: utf-8 -*-
class MySolution(object):
    def rob(self, nums):
        """
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


class Solution(object):

    def rob(self, nums):
        last, now = 0, 0

        for i in nums:
            last, now = now, max(last + i, now)

        return now

# print(Solution2().rob([155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165]))
print(Solution2().rob([1, 3, 9, 3, 1]))
