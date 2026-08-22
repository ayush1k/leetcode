n = int(input('Enter a number'))
original = n
temp = 0
while n > 0 :
    last_digit = n%10
    temp =  temp*10 + last_digit
    n = n//10

print(original == temp)