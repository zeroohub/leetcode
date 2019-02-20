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


class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lptr = i+1
            rptr = len(nums)-1
            while lptr < rptr:
                total = nums[i] + nums[lptr] + nums[rptr]
                if total < 0:
                    lptr += 1
                elif total > 0:
                    rptr -= 1
                else:
                    result.append([nums[i], nums[lptr], nums[rptr]])
                    while lptr < rptr and nums[lptr] == nums[lptr+1]:
                        lptr += 1
                    while lptr < rptr and nums[rptr] == nums[rptr-1]:
                        rptr -= 1
                    lptr += 1
                    rptr -= 1
        return result

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
