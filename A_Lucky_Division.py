def check(n, li):
    result1=''
    result2=''
    num1, num2= li

    if n<num1 and n<num2:
        return 'NO'
    elif n%num1==0 or n%num2==0:
        return "YES"
    else:
        result1= check(n, [num1*10+4, num1*10+7])
        result2= check(n, [num2*10+4, num2*10+7])
    if result1=='YES' or result2=='YES':
        return "YES"
    return "NO"



n= int(input())
print(check(n,[4, 7]))