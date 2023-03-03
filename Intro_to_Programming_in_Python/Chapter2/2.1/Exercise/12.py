import stdio

def f(n):
    sum=0   #总和
    i=0     #按位计数
    temp=0  #临时数
    while n>0:
        temp=n%10
        if i%2 ==0:
            temp*=2
            sum+=temp%10+int(temp/10%10)
        else:
            sum+=temp
        i+=1
        n=int(n/10)
    
    return 10-sum%10

stdio.writeln("请输入一个十位数")
n=stdio.readInt()
stdio.writeln(str(n)+str(f(n)))