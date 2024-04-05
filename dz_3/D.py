def f():
    n, k = map(int, input().split())
    string = input().split()
    s = set()
    for i in range(n):
        if string[i] in s:
            return True
        s.add(string[i])
        if i >= k:
            s.remove(string[i - k])
    return False
if f() == True:
    print("YES")
else:
    print('NO')