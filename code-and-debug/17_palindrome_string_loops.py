def palindrome(s):
    left = 0
    right = len(s) - 1
    s = s.lower()
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

res = palindrome('ANBCDDCBNA')
print(res)