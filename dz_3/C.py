n = int(input())
string = input().split()
d = {}
for i in string:
    if int(i) in d:
        d[int(i)] += 1
    else:
        d[int(i)] = 1
if n > 1 and len(d) != 1:
    max_p = 1
    sorted_items = sorted(d.items())
    sorted_dict = {k: v for k, v in sorted_items}
    for i in sorted_dict:
        if (i + 1) in sorted_dict:
            q = sorted_dict[i] + sorted_dict[i + 1]
            if q > max_p:
                max_p = q
    print(n - max_p)
elif len(d) == 1:
    print(0)
else:
    print(0)