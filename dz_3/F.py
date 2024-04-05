s1 = set(input().split())
s2 = input().split()
d = {}

for i in s1:
    length = len(i)
    if length in d:
        d[length].append(i)
    else:
        d[length] = [i]
for word in s2:
    min_w = word
    for i in range(1, len(word) + 1):
        q = word[:i]
        if len(q) in d and q in d[len(q)]:
            min_w = q
            break
    print(min_w, end=' ')