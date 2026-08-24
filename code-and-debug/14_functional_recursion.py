def func(n):
    if n == 1:
        return 1
    return n+ func(n-1)

num = int(input())
print(func(num))