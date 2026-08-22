# https://leetcode.com/problems/palindrome-number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original = x
        n = len(str(x))
        if n==0 or n==1:
            return True
        result = 0
        while x > 0:
            last_digit = x%10
            result = result*10 + last_digit
            x = x//10

        return original == result
