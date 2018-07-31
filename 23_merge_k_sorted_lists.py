# -*- coding: utf-8 -*-
from data_structure import *


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = result = ListNode(None)

        while lists:
            min_node = None
            min_idx = 0
            for idx, node in enumerate(lists):
                if (not min_node) or (node and node.val < min_node.val):
                    min_node = node
                    min_idx = idx

            result.next = lists.pop(min_idx)
            if min_node and min_node.next:
                lists.append(min_node.next)
            result = result.next

        return head.next


print(Solution().mergeKLists([stringToListNode('[]'), stringToListNode('[]')]))
