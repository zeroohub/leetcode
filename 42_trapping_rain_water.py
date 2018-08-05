# -*- coding: utf-8 -*-
class Solution(object):
    def get_max_idx(self, h):
        return max(enumerate(h), key=lambda x: x[1])

    def trap(self, height):
        if not height:
            return 0
        result = 0
        idx, _ = self.get_max_idx(height)

        left = right = idx
        while left > 0:
            max_idx, _ = self.get_max_idx(height[0:left])
            result += height[max_idx] * (left - max_idx - 1) - sum(height[max_idx+1:left])
            left = max_idx

        while right < len(height)-1:
            max_idx, _ = self.get_max_idx(height[right+1:len(height)])
            max_idx += right + 1
            result += height[max_idx] * (max_idx - right - 1) - sum(height[right+1:max_idx])
            right = max_idx

        return result

class Solution2(object):

    def trap(self, height):
        """
        opt to dp
        https://leetcode.com/problems/trapping-rain-water/solution/
        :param height:
        :return:
        """
        result = 0

        for i in range(len(height)):
            max_left = max_right = 0
            for j in range(0, i+1):
                max_left = max(max_left, height[j])
            for j in range(i, len(height)):
                max_right = max(max_right, height[j])

            result += min(max_right, max_left) - height[i]

        return result

class Solution3(object):

    def trap(self, height):
        """
        use stack
        https://leetcode.com/problems/trapping-rain-water/solution/
        :param height:
        :return:
        """
        result = 0
        stack = []
        current = 0
        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = current - stack[-1] - 1
                bounded_height = min(height[stack[-1]], height[current]) - height[top]
                result += distance * bounded_height

            stack.append(current)
            current += 1

        return result


class Solution4(object):
    """
    TODO
    two pointer solution
    """
    pass


