n= int(input())
price=[]
quality=[]

for i in range(n):
    p, q= map(int , input().split())
    price.append([p, i])
    quality.append([q, i])
price.sort(key= lambda x: x[0])
quality.sort(key=  lambda x:x[0])

for i in range(n):
    if price[i][1]!=quality[i][1]:
        print("Happy Alex")
        break
else:
    print('Poor Alex')