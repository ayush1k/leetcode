# https://www.geeksforgeeks.org/problems/palindrome-string0817/1
class Solution:
    def isPalindrome(self, s):
        # code here
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True
