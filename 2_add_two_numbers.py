# -*- coding: utf-8 -*-
from data_structure import *
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        div = 0
        head = node = ListNode(None)
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            div, mod = divmod(v1 + v2 +div, 10)
            node.next = ListNode(mod)
            node = node.next
            l1 = l1 and l1.next
            l2 = l2 and l2.next

        if div:
            node.next = ListNode(div)

        return head.next


print(Solution().addTwoNumbers(stringToListNode('[1, 2, 3, 4]'), stringToListNode('[8, 9, 3]')))
