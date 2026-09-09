n= int(input())
x=0

for _ in range(n):
    statment= input()
    if '+' in statment:
        x+=1
    else:
        x-=1
print(x)