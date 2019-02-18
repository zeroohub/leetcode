# -*- coding: utf-8 -*-
from math import sqrt
class Solution:
    def countPrimes(self, n: 'int') -> 'int':
        result = 1 if n > 2 else 0
        for i in range(1, n, 2):
            if self.is_prime(i):
                result += 1

        return result

    def is_prime(self, num):
        if num == 1:
            return False

        for i in range(3, int(sqrt(num))+1, 2):
            if num % i == 0:
                return False
        return True


class Solution:
    def countPrimes(self, n: 'int') -> 'int':
        if n < 3:
            return 0
        result = [1] * n
        result[0] = result[1] = 0

        last_prime = 2
        for i in range(2, n):
            if result[i] == 1:
                if n <= last_prime**2:
                    break
                result[i+i:n:i] = [0] * len(result[i+i:n:i])
                last_prime = i

        return sum(result)


print(Solution().countPrimes(10))
