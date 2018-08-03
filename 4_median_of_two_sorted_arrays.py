# -*- coding: utf-8 -*-

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                result.append(nums1[0])
                nums1.pop(0)
            else:
                result.append(nums2[0])
                nums2.pop(0)

        if nums1:
            result += nums1

        if nums2:
            result += nums2

        if len(result) % 2 == 1:
            return result[len(result) // 2]
        else:
            a = len(result) // 2
            return (result[a] + result[a-1]) / 2


class Solution2(object):
    """
    TODO
    https://leetcode.com/problems/median-of-two-sorted-arrays/solution/
    better solution with Math use O(logN)
    """
    def findMedianSortedArrays(self, nums1, nums2):
        pass

print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
