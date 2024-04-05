N = map(int, input().split())
string = input()
m = list(map(int, string.split()))
max_m = max(m)
sum_m = sum(m)
sum_bez_max = sum_m - max_m
if max_m <= sum_bez_max:
    print(sum_m)
else:
    print(max_m - sum_bez_max)
