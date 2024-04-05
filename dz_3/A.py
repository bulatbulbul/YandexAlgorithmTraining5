d = {}
n = int(input())
for i in range(n):
    k = int(input())
    string = input()
    m = list(map(str, string.split()))
    for j in m:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
res = []
for k in d:
    if n == d[k]:
        res.append(k)
res.sort()
print(len(res))
for i in res:
    print(i, end=' ')
