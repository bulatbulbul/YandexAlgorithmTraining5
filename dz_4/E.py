k = int(input())
r = (int(((8 * k - 7) ** 0.5) - 1) // 2) + 1
o = k - (r * (r - 1) // 2)
if r % 2 == 0:
    print(r - o + 1,'/', o,sep='')
else:
    print(o, '/',r - o + 1,sep='')
