n1 = int(input())
s1 = input().split()
ss1 = set(s1)
n2 = int(input())
s2 = input().split()
ss2 = set(s2)
n3 = int(input())
s3 = input().split()
ss3 = set(s3)
d = {}
for i in ss1:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in ss2:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in ss3:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
mas = []
for k in d:
    if d[k] >= 2:
        mas.append(int(k))
mas.sort()
for i in mas:
    print(i,end = ' ')
