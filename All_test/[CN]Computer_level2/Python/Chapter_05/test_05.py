def number(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return number(n-1)+number(n-2)

print(number(6))