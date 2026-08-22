# https://www.geeksforgeeks.org/problems/number-of-factors1435
class Solution:
    def countFactors (self, n):
        # code here
        divisors = 0
        for i in range(1, n//2 + 1):
            if n%i==0:
                divisors +=1
        return divisors+1
