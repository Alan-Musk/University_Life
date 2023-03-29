import stdio
import sys
import math

n=int(sys.argv[1])

a=1
while a<=n:
    a3=a**3
    if a3>n:
        break
    
    b=a
    while b<=n:
        b3=b**3
        if (a3+b3>n):
            break;
        
        c=a+1
        while c<=n:
            c3=c**3
            if c3>a3+b3:
                break;

            d=c
            while d<=n:
                d3=d**3
                if c3+d3>a3+b3:
                    break
                if c3 + d3 == a3 + b3:
                    stdio.write(str(a3+b3) + ' = ')
                    stdio.write(str(a) + '^3 + ' + str(b) + '^3 = ')
                    stdio.write(str(c) + '^3 + ' + str(d) + '^3')
                    stdio.writeln()
                d+=1
            c+=1
        b+=1
    a+=1
            