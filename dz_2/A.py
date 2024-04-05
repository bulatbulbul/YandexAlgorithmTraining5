K = int(input())
min_i, min_j = map(int, input().split())
max_i = min_i
max_j = min_j
for i in range(1, K):
    x_i, x_j = map(int, input().split())
    if x_i > max_i:
        max_i = x_i
    if x_i < min_i:
        min_i = x_i
    if x_j > max_j:
        max_j = x_j
    if x_j < min_j:
        min_j = x_j
print(min_i, min_j, max_i, max_j)
