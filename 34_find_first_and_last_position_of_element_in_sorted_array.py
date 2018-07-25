# -*- coding: utf-8 -*-
class Solution(object):
    def searchRange(self, nums, target):
        """
        easy to understand, but in the worst case, it can use O(n) time
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                left = right = mid
                while left >= 0:
                    if nums[left] == nums[mid]:
                        left -= 1
                    else:
                        break


                while right <= len(nums)-1:
                    if nums[right] == nums[mid]:
                        right += 1
                    else:
                        break

                return [left+1, right-1]

            elif target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1

        return [-1, -1]



class Solution2(object):
    """
    search left end first, than right end.
    """
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]
