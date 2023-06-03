import stdio

x=int(input("请输入一个整数:"))
term=1.0
total=0.0
n=1
while total!=total+term:
    total+=term
    term*=x/n
    n+=1
stdio.writeln(total)

