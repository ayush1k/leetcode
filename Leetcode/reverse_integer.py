# leetcode.com/problems/reverse-integer/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = len(str(x))
        if n == 0 or n == 1:
            return x

        if x > 0:
            result = 0
            while x > 0:
                last_digit = x % 10
                x = x // 10
              
                if result > (2**31 - 1 - last_digit) // 10:
                    return 0

                result = result * 10 + last_digit
            return result
        else:
            x = x * -1          # make x positive
            result = 0
            while x > 0:
                last_digit = x % 10
                x = x // 10
              
                if result > (2**31 - last_digit) // 10:
                    return 0

                result = result * 10 + last_digit
            return result * -1
