# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x.start)
        result = [Interval(intervals[0].start, None)]
        end = intervals[0].end
        for i in intervals:
            if end >= i.start:
                end = max(i.end, end)
            else:
                inte = result.pop()
                inte.end = end
                result.append(inte)
                result.append(Interval(i.start))
                end = i.end

        inte = result.pop()
        inte.end = end
        result.append(inte)

        return result
