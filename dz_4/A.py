def lbinsearch(mas, q):
    l = 0
    r = len(mas)
    while l < r:
        m = l + (r - l) // 2
        if mas[m] < q:
            l = m + 1
        else:
            r = m
    return l

def rbinsearch(mas, q):
    l = 0
    r = len(mas)
    while l < r:
        m = l + (r - l) // 2
        if mas[m] <= q:
            l = m + 1
        else:
            r = m
    return l

n = int(input())
mas = sorted(list(map(int, input().split())))
k = int(input())
for i in range(k):
    l, r = map(int, input().split())
    l_id = lbinsearch(mas,l)
    r_id = rbinsearch(mas,r)
    print(r_id - l_id, end = ' ')

