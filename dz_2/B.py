N, K = map(int, input().split())
string = input()
m = list(map(int, string.split()))
s = 0
for i in range(N):
    for j in range(1, K + 1):
        if i + j <= N - 1:
            if m[i + j] - m[i] > s:
                s = m[i + j] - m[i]
        else:
            break
print(s)