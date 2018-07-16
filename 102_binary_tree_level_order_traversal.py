# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        level_queue = [[root]]

        while level_queue[-1]:
            node_queue = level_queue.pop()
            node_queue_value = []
            next_node_queue = []
            for node in node_queue:
                node_queue_value.append(node.val)
                if node.left:
                    next_node_queue.append(node.left)
                    node.left = None
                if node.right:
                    next_node_queue.append(node.right)
                    node.right = None
            level_queue.append(node_queue_value)
            level_queue.append(next_node_queue)

        level_queue.pop()

        return level_queue
