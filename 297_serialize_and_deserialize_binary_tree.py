# -*- coding: utf-8 -*-
import json
from data_structure import *

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return json.dumps([])

        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)

                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        while result[-1] is None:
            result = result[:-1]

        return json.dumps(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = json.loads(data)
        if not data:
            return None

        root = TreeNode(data.pop(0))
        queue = [root]
        while data:
            node = queue.pop(0)
            if data:
                val = data.pop(0)
                if val is not None:
                    node.left = TreeNode(val)
                    queue.append(node.left)
            if data:
                val = data.pop(0)
                if val is not None:
                    node.right = TreeNode(val)
                    queue.append(node.right)
        return root


