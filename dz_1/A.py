P, V = map(int, input().split())
Q, M = map(int, input().split())
s_1 = 1 + V * 2
s_2 = 1 + M * 2
max_1 = P + V
min_1 = P - V
max_2 = Q + M
min_2 = Q - M
print("min_1 ",min_1)
print("max_1 ",max_1)
print("min_2 ",min_2)
print("max_2 ",max_2)
print("________")
for i in range(2):
    if (min_1 < min_2 and max_1 < min_2):
        print(s_1+s_2)
        print(1)
        break
    elif min_1 < min_2 and max_1 >= min_2 and max_1 < max_2 :
        print(max(max_1,max_2)-min(min_1,min_2)+1)
        print(2)
        break
    elif min_1 >= min_2 and max_2 >= max_1:
        print(s_2)
        print(3)
        break
    max_1,max_2=max_2,max_1
    min_1,min_2=min_2,min_1
    s_1,s_2=s_2,s_1



'''
while V!=-1:
    set_s.add(P-V)
    set_s.add(P+V)
    V-=1
while M!=-1:
    set_s.add(Q-M)
    set_s.add(Q+M)
    M-=1
print(len(set_s))
'''


"""s_1 = 1 + V * 2
s_2 = 1 + M * 2
max_1 = P + V
min_2 = Q - M
if max_1 < min_2:
    print(s_1 + s_2)
else:
    print(s_1 + s_2 + max_1 - min_2 - 1)
"""