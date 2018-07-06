# -*- coding: utf-8 -*-

from data_structure import *

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = None
        while head:
            temp = head.next
            head.next = p
            p = head
            head = temp
        return p
