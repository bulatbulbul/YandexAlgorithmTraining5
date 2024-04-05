n=int(input())
ch=0
for i in range (n):
    x=int(input())
    if x%4==3:
        x+=1
        ch+=1
    if x%4!=3:
        ch+=x//4 + x%4
print(ch)