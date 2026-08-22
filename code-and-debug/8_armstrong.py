def lenght_of_number(num):
    counter = 0
    while num > 0:
        counter += 1
        num = num//10
    return counter
n = int(input())
original = n
result = 0
num_len = lenght_of_number(original)
while n > 0:
    ld = n%10
    result = result + ld**num_len
    n = n//10

print(original == result)

# can also find the lenght of number using len(str(num))