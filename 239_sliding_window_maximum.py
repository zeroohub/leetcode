# -*- coding: utf-8 -*-
import collections
from bisect import *
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        result = []
        left = 0
        right = k
        dpk = sorted(nums[:k])
        result.append(dpk[-1])

        while right < len(nums):
            insort_right(dpk, nums[right])
            idx = bisect_left(dpk, nums[left])
            dpk.pop(idx)
            result.append(dpk[-1])
            right += 1
            left += 1

        return result

import collections

class Solution2(object):
    def maxSlidingWindow(self, nums, k):
        """
        https://leetcode.com/problems/sliding-window-maximum/discuss/65884/Java-O(n)-solution-using-deque-with-explanation
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = collections.deque()
        ans = []
        for i in range(len(nums)):

            # remove number out of range
            while dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)
            if i >= k - 1:
                ans.append(nums[dq[0]])
        return ans
