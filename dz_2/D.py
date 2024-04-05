N = int(input())
i, j = map(int, input().split())
m = [[i, j]]
s = 4
for x in range(1, N):
    i, j = map(int, input().split())
    m.append([i, j])
for i in range(N - 1):
    if m[i][0] == m[i + 1][0]:
        if (m[i + 1][1] - m[i][1]) == 1:
            s += 2
        else:
            s += 4
    else:
        s += 4
for i in range(N - 1):
    for j in range(i + 1, N):
        if (m[i][0] + 1) == m[j][0] and m[i][1] == m[j][1]:
            s -= 2
print(s)
