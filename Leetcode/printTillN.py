# https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops3621/1
class Solution:
    def printTillN(self, n):
    	#code here
    	if n == 0:
    	    return
    	self.printTillN(n-1)
    	print(n, end=' ')
