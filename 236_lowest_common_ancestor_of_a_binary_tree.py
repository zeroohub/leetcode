# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.q = q
        self.p = p
        self.find = False
        return self.travel(root)


    def travel(self, root):
        if not root:
            return
        if root.val == self.q.val:
            return self.q
        if root.val == self.p.val:
            return self.p

        left = self.travel(root.left)
        if self.find:
            return left
        right = self.travel(root.right)
        if self.find:
            return right


        co = {self.q, self.p}
        if {left, right} == co:
            self.find = True
            return root
        if left in co:
            return left
        if right in co:
            return right
        return root

