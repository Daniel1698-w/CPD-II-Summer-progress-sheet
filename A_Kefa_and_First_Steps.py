n= int(input())
lis = list(map(int ,input().split()))
_max=1
count=1

for i in range(1, n):
    if lis[i]>=lis[i-1]:
        count+=1
        _max= max(_max, count)
    else:
        count=1
print(_max)