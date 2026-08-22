# brute force
# num = int(input())
# divisors = []
# for i in range(1, num+1):
#     if num % i == 0:
#         divisors.append(i)
# divisors.append(num)

# print(divisors)




# better
# num = int(input())
# divisors = []
# for i in range(1, num//2 +1):
#     if num % i == 0:
#         divisors.append(i)
# divisors.append(num)

# print(divisors)

# optimal solution
from math import sqrt
num = int(input())
divisors = []
for i in range(1, int(sqrt(num))+1):
    if num%i==0:
        divisors.append(i)
        if num//i != i:
            divisors.append(num//i)

print(divisors)