string= input()
n= int(input())

prefix_sum=[0]*(len(string)+1)

for i in range(len(string)-1):
    prefix_sum[i+1]= prefix_sum[i]
    if string[i]==string[i+1]:
        prefix_sum[i+1]+=1

for i in range(n):
    l, r= map(int , input().split())
    print(prefix_sum[r-1]-prefix_sum[l-1])

    
