# -*- coding: utf-8 -*-
class MySolution(object):
    def canPartition(self, nums):
        """
        Failed, wrong way
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        left = 0
        right = len(nums)-1
        outer_sum = 0
        inner_sum = sum(nums)
        while right > 0:
            if left == 0:
                while left < right:
                    inner_sum -= nums[left]
                    outer_sum += nums[left]
                    if outer_sum == inner_sum:
                        return True
                    left += 1
            elif left == right:
                while left >= 0:
                    inner_sum += nums[left]
                    outer_sum -= nums[left]
                    if outer_sum == inner_sum:
                        return True
                    left -= 1

            right -= 1
            outer_sum += nums[right]
            inner_sum -= nums[right]

        return False


class Solution(object):
    """
    DP solution, iterative
    list sort reverse or not, doesn't affect result, just speed.
    """
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 == 1:
            return False
        nums.sort(reverse=True)
        target = total // 2
        if nums[0] > total:
            return False

        dp = [False for i in range(target + 1)]
        dp[0] = True
        for n in nums:
            for t in range(target, n-1, -1):
                dp[t] = dp[t] or dp[t-n]
                if dp[target]:
                    return True

        return False


class Solution2(object):
    def canPartition(self, nums):
        """
        DP solution, recursive
        if not reverse sort list, will exceed time limit
        :type nums: List[int]
        :rtype: bool
        """

        nums.sort(reverse=True)
        total = sum(nums)
        if total % 2 == 1:
            return False
        if nums[0] > total / 2:
            return False

        def backtrack(start, target):
            if target < 0:
                return False
            if target == 0:
                return True
            for i in range(start, len(nums)):
                if backtrack(i+1, target - nums[i]):
                    return True
            return False
        return backtrack(0, total // 2)

print(Solution().canPartition([1, 2, 3, 4, 5, 6, 7]))
