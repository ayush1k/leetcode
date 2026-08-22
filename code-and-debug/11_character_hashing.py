s = 'azyuyyzaaaa'
q = ['d', 'a', 'y', 'z']
freq = {}
for i in range(0, len(s)):
    freq[s[i]] = freq.get(s[i], 0) + 1

print(freq)
for i in q:
    print(i, '-->', freq.get(i))