import math

lis=[]
for _ in range(3):
    lis.append(int(input()))

if lis.count(1)==3:
    print(sum(lis))
elif lis.count(1)==0:
    print(math.prod(lis))
else:
    val1= (lis[0]+lis[1])*lis[2]
    val2= lis[0]*(lis[1]+lis[2])
    val3= sum(lis)
    print(max(val1, val2, val3))