# -*- coding: utf-8 -*-
class Solution(object):
    def maxArea(self, height):
        """
        fail to pass, don't know why
        :type height: List[int]
        :rtype: int

        """

        asc_height = [0 for i in range(len(height))]

        highest = 0
        max_sq = 0
        for i, h in enumerate(height):
            if not h:
                continue
            prev_sq = -1
            for j in range(len(asc_height)-1, -1, -1):
                if asc_height[j] == 0:
                    continue
                sq = (i - j) * min(asc_height[j], h)
                max_sq = max(sq, max_sq)
                if sq > prev_sq:
                    prev_sq = sq
                else:
                    asc_height[j] = 0

            if h > highest:
                highest = h
                asc_height[i] = h
        return max_sq


class Solution2(object):
    """
    two pointer from solution
    """
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_sq = -1
        while left < right:
            sq = (right - left) * min(height[left], height[right])
            max_sq = max(max_sq, sq)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_sq

