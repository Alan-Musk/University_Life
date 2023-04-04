import stdio
def chaos(x,r,t):
    time=0
    while time<t:
        if(x==(1-1/r)):
            break
        time+=1
        x=r*x*(1-x)
    return x

t=1000
r=1.0
while r<10:
    r+=0.1
    x=0.01
    x=chaos(x,r,t)
    if(x==(1-1/r)):
        stdio.writeln("当r={:1f}时x稳定在x=1-1/r={:3f}".format(r,x))
stdio.writeln(chaos(0.01,3.5,1000))
stdio.writeln(chaos(0.01,3.8,1000))
stdio.writeln(chaos(0.01,5,1000))


        
