# -*- coding: utf-8 -*-

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.reverse()
        result = []
        for i in range(len(nums)):
            temp = 0
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    temp += 1
            result.append(temp)
        result.reverse()
        return result


class Solution2:
    def merge_sort(self, nums):
        """
        TODO
        https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76583/11ms-JAVA-solution-using-merge-sort-with-explanation
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            return [min(nums), max(nums)]

        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        result = []
        li = ri = 0
        while li < len(left) and ri < len(right):
            if left[li] < right[ri]:
                result.append(left[li])
                li += 1
            else:
                result.append(right[ri])
                ri += 1

        if li < len(left):
            result += left[li:]
        if ri < len(right):
            result += right[ri:]

        return result

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.reverse()
        result = []
        for i in range(len(nums)):
            temp = 0
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    temp += 1
            result.append(temp)
        result.reverse()
        return result

class TreeNode:
    def __repr__(self) -> str:
        return "val: {}, count: {}, leftsize: {}".format(self.val, self.count, self.left_size)

    def __init__(self, val) -> None:
        self.val = val
        self.left_size = 0
        self.count = 1
        self.right = None
        self.left = None

    def insert(self, val):
        if val == self.val:
            self.count += 1
            return self.left_size
        elif val < self.val:
            self.left_size += 1
            if not self.left:
                self.left = TreeNode(val)
                return 0
            return self.left.insert(val)
        elif val > self.val:
            if not self.right:
                self.right = TreeNode(val)
                return self.count + self.left_size
            return self.count + self.left_size + self.right.insert(val)

class Solution3:
    def countSmaller(self, nums):
        if not nums:
            return []
        nums.reverse()
        root = TreeNode(nums[0])
        result = [0] + [root.insert(n) for n in nums[1:]]
        result.reverse()
        return result

print(Solution3().countSmaller([76, 99, 51, 9, 21, 84, 66, 65, 36,100, 41]))
