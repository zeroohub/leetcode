# -*- coding: utf-8 -*-
class Solution(object):
    """
    f(1) = 1
    f(2) = 2
    f(n) = f(n-1) + f(f-2)
    """
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        fn1 = 1
        fn2 = 2
        fn3 = 0
        for i in range(3, n+1, 1):
            fn3 = fn1 + fn2
            fn1 = fn2
            fn2 = fn3

        return fn3

