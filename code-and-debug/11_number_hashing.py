n = [5,3,2,2,1,5,5,6,7,3,4,6,8,9]
m = [10,111,9,5,67,2]
freq = {}
for i in range(0, len(n)):
    freq[n[i]] = freq.get(n[i], 0) + 1

print(freq)

for nums in m:
    if nums < 1 and nums > len(n):
        print(0)
    else:
        print(nums, '--' ,freq.get(nums))
