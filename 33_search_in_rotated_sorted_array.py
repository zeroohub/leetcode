# -*- coding: utf-8 -*-

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.find(nums, 0, len(nums)-1, target)

    def find(self, nums, start, end, target):
        if end - start == 0:
            if target != nums[end]:
                return -1
            else:
                return end

        mid = start + (end - start) // 2
        if target <= nums[mid] and nums[start] <= nums[end]:
            return self.find(nums, start, mid, target)
        elif target > nums[mid] and nums[start] <= nums[end]:
            return self.find(nums, mid+1, end, target)
        else:
            s = self.find(nums, start, mid, target)
            b = self.find(nums, mid+1, end, target)
            return max(s, b)


class Solution2(object):
    """
    smarter way
    https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
    """
    def search(self, nums, target):
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if target < nums[0]:
                if nums[mid] < nums[0]:
                    temp = nums[mid]
                else:
                    temp = -float('inf')
            elif target == nums[0]:
                return 0
            else:
                if nums[mid] >= nums[0]:
                    temp = nums[mid]
                else:
                    temp = float('inf')

            if temp < target:
                low = mid + 1
            elif temp > target:
                high = mid - 1
            else:
                return mid

        return -1


print(Solution().search([4,5,6,7,0,1,2], 3))
