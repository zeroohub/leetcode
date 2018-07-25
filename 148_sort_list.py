# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.merge(head)

    def merge(self, head):
        if not head or not head.next:
            return head

        if head and head.next and not head.next.next:
            if head.val > head.next.val:
                temp = head.next
                head.next = None
                temp.next = head
                return temp
            return head

        h1, h2 = self.split(head)
        h1 = self.merge(h1)
        h2 = self.merge(h2)
        th1 = ListNode(None)
        th2 = th1
        while h1 and h2:
            if h1.val > h2.val:
                th1.next = h2
                h2 = h2.next
            else:
                th1.next = h1
                h1 = h1.next
            th1 = th1.next
        if h1:
            th1.next = h1
        if h2:
            th1.next = h2

        return th2.next


    def split(self, head):
        slow = fast = head
        pre = None
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next

        pre.next = None

        return head, slow


print(Solution().sortList(stringToListNode('[-1,5,3,4,0]')))
