string= input().lower()
vowels= set(['a', 'e', 'o', 'u', 'i', 'y'])
ans=''

for i in string:
    if i not in vowels:
        ans+='.'+ i
        
print(ans)
