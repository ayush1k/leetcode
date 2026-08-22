# https://www.geeksforgeeks.org/problems/print-gfg-n-times/1
n = int(input())

# Code here
def func(n):
    if n == 0:
        return
    print('GFG', end=" ")
    func(n-1)

func(n)
