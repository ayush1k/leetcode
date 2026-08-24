def palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False

    return palindrome(s, left + 1, right - 1)

user_string = 'ANBCDDCBNA'
n = len(user_string)
res = palindrome(user_string, left=0, right = n - 1)
print(res)
