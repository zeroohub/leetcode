# -*- coding: utf-8 -*-
from data_structure import *

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        self.result = None
        self.values = [p.val, q.val]
        self.DFS(root)
        return self.result

    def DFS(self, node):
        if not node:
            return 0
        left_find = self.DFS(node.left)

        node_find = 1 if self.find(node) else 0
        right_find = self.DFS(node.right)
        if not self.result:
            if left_find == 2:
                self.result = node.left
            elif right_find == 2:
                self.result = node.right
            elif right_find + left_find + node_find == 2:
                self.result = node

        return right_find + left_find + node_find

    def find(self, node):
        if node.val in self.values:
            return True
        return False

class Solution:

    def lowestCommonAncestor(self, root, p, q):

        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root



print(Solution().lowestCommonAncestor(stringToTreeNode("[41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23]"), TreeNode(40), TreeNode(46)))
