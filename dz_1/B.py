s1=str(input())
k1_1=float(s1[0])
k2_1=float(s1[2])
s2=str(input())
k1_2=float(s2[0])
k2_2=float(s2[2])
l=int(input())
ch=0
if l==1:
    k2_1*=1.01
    k1_2*=1.01
    while ((k2_1+k2_2) >= (k1_1+k1_2)):
        k1_2+=1.01
        ch+=1
else:
    k1_1*=1.01
    k2_2*=1.01
    while ((k2_1+k2_2) >= (k1_1+k1_2)):
        k1_2+=1
        ch+=1
print(ch)