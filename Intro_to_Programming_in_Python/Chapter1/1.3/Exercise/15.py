import sys
import stdio

n=int(sys.argv[1])

i=1
j=1
while i<n+1:
    j=1
    while j<n+1:
        if(i%j==0 or j%i==0):
            stdio.write(' * ')
        else:
            stdio.write('   ')
        j+=1
    stdio.writeln(i)
    i+=1
    
        
    
    
    