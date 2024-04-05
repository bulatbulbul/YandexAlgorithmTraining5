def f_sum(k):
    sum1 = k * (k + 1) // 2
    sum2 = k * (k + 1) * (2 * k + 1) // 6
    result = (k + 1) * sum1 - sum2
    return result

def arif_p(k):
    return int(k*(k+1)/2) - 1

n = int(input())
for k in range (10**10):
    if (f_sum(k) + arif_p(k)) <= n < (f_sum(k+1) + arif_p(k+1)):
        print(k)
        break
