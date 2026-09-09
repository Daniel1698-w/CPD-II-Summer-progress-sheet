n= int(input())

count=0

for i in range(n):
    line= list(map(int, input().split()))
    if line.count(1)>=2:
        count+=1
print(count)