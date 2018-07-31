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
            min_idx = 0
            for idx in range(len(lists)):
                if not lists[idx]:
                    continue
                if lists[min_idx] and lists[idx].val < lists[min_idx].val:
                    min_idx = idx

            min_node = lists.pop(min_idx)
            if min_node:
                result.next = min_node
                result = result.next
                lists.append(min_node.next)

        return head.next


class Solution2(object):
    def mergeKLists(self, lists):
        """
        divide and conquer
        https://leetcode.com/problems/merge-k-sorted-lists/solution/
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next


print(Solution().mergeKLists([stringToListNode('[]'), stringToListNode('[1]')]))
