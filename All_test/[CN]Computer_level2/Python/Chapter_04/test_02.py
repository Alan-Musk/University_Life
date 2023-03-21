num1=int(input())
num2=int(input())

def max(num1,num2):
    if(num1<num2):
        num1,num2=num2,num1
    if(num1%num2==0):
        return num2
    else:
        num1,num2=num2,num1%num2
        return max(num1,num2)

print("最大公约数是:",max(num1,num2))
print("最小公倍数是:",(num1*num2)/max(num1,num2))




