n, m = map(int, input().split())
mas = list(map(int, input().split()))
mas_q = [tuple(map(int, input().split())) for _ in range(m)]
mas_s = [0] * (n + 1)
for i in range(1, n + 1):
    mas_s[i] = mas_s[i - 1] + mas[i - 1]
for q in mas_q:
    l, s = q
    left = 0
    right = n - l
    result = -1
    while left <= right:
        mid = (left + right) // 2
        subarray_sum = mas_s[mid + l] - mas_s[mid]
        if subarray_sum < s:
            left = mid + 1
        elif subarray_sum > s:
            right = mid - 1
        else:
            result = mid
            break
    if result != -1:
        print(result + 1)
    else:
        print(-1)
