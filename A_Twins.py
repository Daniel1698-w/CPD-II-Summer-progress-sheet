n= int(input())
lis= list(map(int ,input().split()))
lis.sort(reverse=True)

total_sum= sum(lis)
sum=0
count=0
i=0

while i<n and sum<=total_sum:
    sum+=lis[i]
    total_sum-= lis[i]
    count+=1
    i+=1

print(count)