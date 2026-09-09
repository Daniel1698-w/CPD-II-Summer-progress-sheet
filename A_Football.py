line= input()
count=1

for i in range(1,len(line)):
    if line[i]==line[i-1]:
        count+=1
    else:
        count=1
    if count>=7:
        print('YES')
        break
else:
    print('NO')