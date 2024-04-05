n, k, d = map(int, input().split())
new_n = ''
new_n_2 = 0
for i in range(10):
    if (int(str(n) + str(i) ) % k) == 0:
        new_n = str(n) + str(i)
        new_n_2 = n * 10 + i
        break
if new_n_2 == 0 or len(str(n))==len(str(new_n_2)):
    print(-1)
else:
    for i in range (d-1):
        new_n+='0'
    print(new_n)


