# -*- coding: utf-8 -*-
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def listToll(nums):
    nodes = [ListNode(n) for n in nums]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    return nodes[0]


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A = []
        while headA:
            A.append(headA)
            headA = headA.next

        B = []
        while headB:
            B.append(headB)
            headB = headB.next

        if len(A) == 0 or len(B) == 0:
            return None

        if len(A) == 1 or len(B) == 1:
            if A[-1] == B[-1]:
                return A[-1]

        for i in range(-1, -min(len(A), len(B)), -1):
            if A[i] == B[i]:

                if A[i-1] == B[i-1]:
                    if i == -min(len(A), len(B)) + 1:
                        return A[i-1]
                    continue
                return A[i]

