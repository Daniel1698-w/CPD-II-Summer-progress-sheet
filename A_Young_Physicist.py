n= int(input())
lis=[0, 0 ,0]

for _ in range(n):
    line= list(map(int , input().split()))
    lis[0]+= line[0]
    lis[1]+= line[1]
    lis[2]+= line[2]
    
if lis[0]==lis[1]==lis[2]==0:
    print("YES")
else:
    print("NO")
