# -*- coding: utf-8 -*-
from collections import defaultdict

class MyMinStack(object):

    def __init__(self):
        self._stack = []
        self._minCounter = defaultdict(int)
        self._minList = []
        """
        initialize your data structure here.
        """

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)
        self._minCounter[x] += 1
        if len(self._minList) == 0:
            self._minList.append(x)
        elif self._minCounter[x] == 1:
            if x > self._minList[0]:
                self._minList.append(x)
            elif x < self._minList[0]:
                self._minList.insert(0, x)
            else:
                for i in range(len(self._minList) - 1):
                    if x > self._minList[i] and x < self._minList[i+1]:
                        self._minList.insert(i+1, x)
                        break

    def pop(self):
        """
        :rtype: void
        """
        if len(self._stack) == 0:
            return None
        p = self._stack.pop()
        if self._minCounter[p] == 1:
            del self._minCounter[p]
            self._minList.remove(p)
        else:
            self._minCounter[p] -= 1


    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1] if len(self._stack) > 0 else None

    def getMin(self):
        """
        :rtype: int
        """
        return self._minList[0]


class MinStack2(object):

    def __init__(self):
        self._stack = []
        self._minStack = []
        """
        initialize your data structure here.
        """

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = x
        if self._stack:
            preMin = self._minStack[-1]
            curMin = min(curMin, preMin)
        self._stack.append(x)
        self._minStack.append(curMin)

    def pop(self):
        """
        :rtype: void
        """
        self._minStack.pop()
        return self._stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1] if self._stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self._minStack[-1]
