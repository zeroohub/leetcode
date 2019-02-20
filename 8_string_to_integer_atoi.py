# -*- coding: utf-8 -*-
class Solution(object):
    def myAtoi(self, str):
        int_max = 2**31 - 1
        int_min = -2**31
        """
        :type str: str
        :rtype: int
        """
        strl = list(str)
        result = ""
        while strl:
            char = strl.pop(0)
            if char == " ":
                if result:
                    break
                else:
                    continue
            elif char.isalpha():
                if not result:
                    return 0
                else:
                    break
            elif char.isdigit():
                result += char
            elif char in ("+", "-"):
                if not result:
                    result += char
                else:
                    break
            else:
                break

        try:
            re = int(result)
            if re >= int_max:
                return int_max
            if re <= int_min:
                return int_min
            return re
        except:
            return 0

print(Solution().myAtoi('3.141'))
