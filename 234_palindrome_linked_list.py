# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MySolution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        plist = []
        while head:
            plist.append(head.val)
            head = head.next

        size = len(plist)
        if size % 2 == 1:
            # 奇数
            if size == 1:
                return True

            midIdx = (size - 1) // 2
            for i in range(midIdx+1):
                if plist[midIdx+i] != plist[midIdx-i]:
                    return False
            return True
        else:
            if size == 0:
                return True

            midIdx2 = size // 2
            midIdx1 = midIdx2 - 1
            for i in range(midIdx1+1):
                if plist[midIdx1-i] != plist[midIdx2+i]:
                    return False
            return True


class Solution2(object):
    """
    this one use one nature of Palindrome, which is
    if you iterate the whole list reverse, it should be the same
    as original list
    """
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        walker = head
        stack = []
        while walker is not None:
            stack.append(walker.val)
            walker = walker.next

        walker = head
        while (stack):
            val = stack.pop()
            if (val != walker.val):
                return False
            walker = walker.next

        return True
