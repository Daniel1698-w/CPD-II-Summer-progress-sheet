from math import ceil
n= int(input())

lis= list(map( int , input().split()))
ones= lis.count(1)
twos=lis.count(2)
threes= lis.count(3)
fours=lis.count(4)

count= fours

count+= threes
ones-= min(threes, ones)
count+= ceil((ones+2*twos)/4)

print(count)
