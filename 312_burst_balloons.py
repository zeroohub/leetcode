# -*- coding: utf-8 -*-
class Solution(object):
    def maxCoins(self, nums):
        """
        brute force
        :type nums: List[int]
        :rtype: int
        """
        final = 1
        while nums:
            maxi = 1
            maxi_idx = 0
            for idx, num in enumerate(nums):
                left = nums[idx-1] if idx-1 >=0 else 1
                right = nums[idx+1] if idx+1 < len(nums) else 1
                result = left * right * num
                if result > maxi:
                    maxi = result
                    maxi_idx = idx

            final += maxi
            nums.pop(maxi_idx)

        return final



print(Solution().maxCoins([3,1,5,8]))
