# -*- coding: utf-8 -*-
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True

        count = 0
        nums.reverse()
        for n in nums[1:]:
            if n == 0:
                count += 1
            else:
                if n > count:
                    count = 0
                if count != 0:
                    count += 1
        return count == 0

print(Solution().canJump([2, 0, 1,0,1]))
