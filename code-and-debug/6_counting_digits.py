num = int(input('Enter a number'))
counter = 0
while num > 0 :
    # last_digit = num%10
    counter += 1
    num = num//10

print(counter)