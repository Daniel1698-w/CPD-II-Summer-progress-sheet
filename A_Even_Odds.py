n, k= map(int , input().split())
half= n//2 +n%2
ans=0

if k<=half:
    ans= 2*k -1
else:
    ans= 2*(k-half)
print(ans)


