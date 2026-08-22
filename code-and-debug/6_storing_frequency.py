# method 1

nums = [1,2,3,4,5,6,7,8,9,1,3,5,7,9]
freq = {}
# for i in range(0, len(nums)):
#     if nums[i] in freq:
#         freq[nums[i]] +=1
#     else:
#         freq[nums[i]] = 1

# print(freq)

# method 2
n = len(nums)
for i in range(0, n):
    freq[nums[i]] = freq.get(nums[i], 0) + 1

print(freq)

# there is almost no differnce in both the codes