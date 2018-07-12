# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    """
    same DP solution, just add width first traversing
    ERROR: misunderstand question, result error
    """
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        layer_queue = [[root]]
        prev = curr = 0

        while layer_queue:
            node_queue = layer_queue.pop()
            next_node_queue = []
            node_sum = 0
            while node_queue:
                node = node_queue.pop()
                node_sum += node.val
                if node.left:
                    next_node_queue.append(node.left)
                if node.right:
                    next_node_queue.append(node.right)

            temp = curr
            curr = max(prev + node_sum, curr)
            prev = temp

            if next_node_queue:
                layer_queue.append(next_node_queue)

        return curr

Solution().rob(stringToTreeNode('[2,1,3,null,4]'))
