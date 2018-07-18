# -*- coding: utf-8 -*-
from collections import Counter, defaultdict

def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


class MySolution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks:
            return 0

        if n == 0:
            return len(tasks)

        c = Counter(tasks)
        if n > len(c):
            mc = c.most_common()
            mv = 0
            for _, v in mc:
                if v == mc[0][1]:
                    mv += 1
                else:
                    break
            return (1+n) * (mc[0][1] - 1) + mv
        else:
            result = []
            most_common = c.most_common()
            wait = defaultdict(int)
            lm = len(most_common)
            while most_common[0][1] != 0:
                for idx in range(lm):
                    t, v = most_common[idx]
                    if t in wait:
                        if idx == lm - 1:
                            result.append(None)
                            for w in list(wait.keys()):
                                wait[w] -= 1
                                if wait[w] == 0:
                                    del wait[w]

                        continue

                    for w in list(wait.keys()):
                        wait[w] -= 1
                        if wait[w] == 0:
                            del wait[w]
                    wait[t] = n

                    most_common[idx] = t, v-1
                    while idx < lm -1 and most_common[idx][1] < most_common[idx + 1][1]:
                        swap(most_common, idx, idx+1)
                        idx += 1
                    result.append(t)
                    break

            return len(result)


class MySolution2(object):
    """
    inspired by solution from discuss
    https://leetcode.com/problems/task-scheduler/discuss/104496/concise-Java-Solution-O(N)-time-O(26)-space

    """
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks:
            return 0

        if n == 0:
            return len(tasks)

        c = Counter(tasks)
        mc = c.most_common()
        mv = 0
        for _, v in mc:
            if v == mc[0][1]:
                mv += 1
            else:
                break
        return max((1+n) * (mc[0][1] - 1) + mv, len(tasks))
